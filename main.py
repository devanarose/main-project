from flask import Flask
from public import public
from admin import admin
from patient import patient
from staff import staff
from doctor import doctor

app=Flask(__name__)
app.secret_key='sk'

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(patient)
app.register_blueprint(staff)
app.register_blueprint(doctor)


app.run(debug=True,port='5000')