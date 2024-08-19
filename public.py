from flask import *
from database import *


public=Blueprint('public',__name__)


@public.route('/')
def home():
    return render_template("home.html")

@public.route('/login',methods=['get','post'])
def login():
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']

        qry1="select * from login where username='%s' and password='%s'"%(username,password)
        res1=select(qry1)
        if res1:
            session['log']=res1[0]['login_id']
            if res1[0]['usertype'] == 'admin':
                return redirect(url_for('admin.admin_home'))
            if res1[0]['usertype'] == 'user':
                qry2="select * from user where login_id='%s'"%(session['log'])
                res2=select(qry2)
                if res2:
                    session['user'] = res2[0]['user_id']
                    return redirect(url_for('users.user_home'))



    return render_template("login.html")

@public.route('/registration',methods=['get','post'])
def registration():
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']

        qry1="insert into login values(null,'%s','%s','user')"%(username,password)
        res1=insert(qry1)

        qry2="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(res1,fname,lname,place,phone,email)
        insert(qry2)
        return redirect('/')

    return render_template("registration.html")

