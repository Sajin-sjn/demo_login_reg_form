from flask import *
from database import *
# from public import login_required 

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')

def admin_home():
    
    return render_template("admin_home.html")

@admin.route('/admin_view_users',methods=['get','post'])
def admin_view_users():
    data={}
    qry1="select * from user"
    res1=select(qry1)
    # print(res1,"________________________")
    if res1:
        data['view']=res1
        print(data['view'],"+++++++++++++++++++++++++++++")

    if 'action' in request.args:
        action=request.args['action']
        user_id=request.args['user_id']

        if action=='update':
            qry2="select * from user where user_id='%s'"%(user_id)
            res2=select(qry2)
            if res2:
                data['up']=res2

                if 'update' in request.form:
                    fname=request.form['fname']
                    place=request.form['place']
                    phone=request.form['phone']

                    qry3="update user set fname='%s',place='%s',phone='%s' where user_id='%s'"%(fname,place,phone,user_id)
                    res3=update(qry3)
                    if res3:
                        return ("<script>alert('updation success');window.location='/admin_view_users'</script>")
                    
    return render_template("admin_view_users.html",data=data)



@admin.route('/view_users',methods=['get','post'])
def view_users():
    data={}
    qry1="select * from user"
    res1=select(qry1)
    # print(res1,"________________________")
    if res1:
        data['view']=res1
        print(data['view'],"+++++++++++++++++++++++++++++")

    if 'action' in request.args:
        action=request.args['action']
        user_id=request.args['user_id']

        if action=='update':
            qry2="select * from user where user_id='%s'"%(user_id)
            res2=select(qry2)
            if res2:
                data['up']=res2

                if 'update' in request.form:
                    fname=request.form['fname']
                    place=request.form['place']
                    phone=request.form['phone']

                    qry3="update user set fname='%s',place='%s',phone='%s' where user_id='%s'"%(fname,place,phone,user_id)
                    res3=update(qry3)
                    if res3:
                        return ("<script>alert('updation success');window.location='/view_users'</script>")
                    
    return render_template("view_users.html",data=data)

