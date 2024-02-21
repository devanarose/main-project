from flask import *
from database import*
public=Blueprint('public',__name__)

# @public.route('/')
# def home():
#     return render_template('home.html')

@public.route('/')
def home():
    
    return render_template('home.html')
@public.route('/speciality')
def speciality():
    data={}
    val = int(request.args['val'])
    print(val)
    if val == 1:
        q="select * from tbl_doctor where doc_specialization ='GENERAL OPHTHALMOLOGY'"
        data['sp']='GENERAL OPHTHALMOLOGY'
    elif val == 2:
        q="select * from tbl_doctor where doc_specialization ='LASER VISION CORRECTION'"
        data['sp']='LASER VISION CORRECTION'
    elif val ==3:
        q="select * from tbl_doctor where doc_specialization ='VITREO RETINA'"  
        data['sp']='VITREO RETINA' 
    elif val ==4:
        q="select * from tbl_doctor where doc_specialization ='CATARACT & GLAUCOMA'"  
        data['sp']='CATARACT & GLAUCOMA' 
    elif val ==5:
        q="select * from tbl_doctor where doc_specialization ='PAEDIATRIC OPHTHALMOLOGY'"  
        data['sp']='PAEDIATRIC OPHTHALMOLOGY'
    elif val ==6:
        q="select * from tbl_doctor where doc_specialization ='ORBIT & OCULOPLASTY'"  
        data['sp']='ORBIT & OCULOPLASTY'
    res=select(q)
    print(q) 
    data['doc']=res
    return render_template('speciality.html',data=data)
@public.route('/contact')
def contact():
    return render_template('contact.html')
# @public.route('/login',methods=['post','get'])
# def login():
# 	if "button" in request.form:
# 		e=request.form['uname']
# 	    p=request.form['password']
	
        
#         q="select * from tbl_login where username='%s' and password='%s'"%(e,p)
#             res=select(q)
#         if res:
#             session['logid']=res[0]['username']
            
#             if res[0]['usertype']=="admin":
#                 return redirect(url_for('admin.admin_home'))

# 			elif res[0]['usertype']=="Patient":
# 				return redirect(url_for('patient.patient_home'))
# 			elif res[0]['usertype']=="staff":
# 				return redirect(url_for('staff.staff_home'))
# 			elif res[0]['usertype']=="doctor":
# 				return redirect(url_for('doctor.doctor_home'))
			
#     return render_template('login.html')
@public.route('/patient',methods=['post','get'])
def patient():
    data={}
    q="select * from tbl_patient"
    res=select(q)
    data['patientview']=res
    
    if "patient" in request.form:
        e=request.form['email']
        fn=request.form['fname']
        ln=request.form['lname']
        pdob=request.form['p_dob']
        pg=request.form['pgender']
        hn=request.form['hname']
        d=request.form['District']
        pin=request.form['pincode']
        phone=request.form['phno']
        p=request.form['password']
        
        import random

        # Generate a random 4-digit integer between 1000 and 9999
        random_number = "PAT"+str(random.randint(1000, 9999))
        print(random_number)


        print(e,fn,ln,pdob,pg,hn,d,pin,phone,p)
        r="select * from tbl_patient where username='%s' or patient_phno='%s'"%(e,phone)
        res=select(r)
        if res:
            flash("Patient already registered")
            return redirect(url_for("public.home"))
        else:
            q="insert into tbl_login values('%s','%s','Patient')"%(e,p)
            res=insert(q)
        
            q="INSERT INTO tbl_patient values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','1','%s')"%(e,fn,ln,pdob,pg,hn,d,pin,phone,random_number)
            insert(q)
            flash("Registered successfuly")
    return render_template('patient.html')




@public.route('/login',methods=['get','post'])
def login():
    if 'button' in request.form:
        e=request.form['uname']
        p=request.form['password']
        q="select * from tbl_login where username='%s' and password='%s'"%(e,p)
        res=select(q)
        
        if res:
            session['logid']=res[0]['username']
            if res[0]['usertype']=="admin":
                return redirect(url_for('admin.admin_home'))
            elif res[0]['usertype']=="Patient":
                q="select * from tbl_patient where username='%s' and status=1"%(session['logid'])
                res=select(q)
                if res:
                    
                    session['pat_id']=res[0]['patient_id']
                    return redirect(url_for('patient.patient_home'))
            elif res[0]['usertype']=="staff":
                q="select * from tbl_staff where staff_status=1 and username='%s'"%(session['logid'])
                res=select(q)
                if res:
                    
                    return redirect(url_for('staff.staff_home'))
            elif res[0]['usertype']=="doctor":
                q="select * from tbl_doctor where doc_status=1 and username='%s' "%(session['logid'])
                res2=select(q)
                if res2:
                    session['docid']=res2[0]['doc_id']
                    return redirect(url_for('doctor.doctor_home'))
        flash("Invalid username or password")
        return render_template('login.html') 
    return render_template('login.html')