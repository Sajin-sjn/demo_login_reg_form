from flask import *
from database import *

users=Blueprint('users',__name__)

@users.route('/user_home',methods=['get','post'])
def user_home():
    return render_template("user_home.html")