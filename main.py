from flask import *
from public import public
from database import *
from admin import admin
from user import users


app=Flask(__name__)




app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(users)
app.secret_key="hhkk"



app.run(debug=True,port=5003)