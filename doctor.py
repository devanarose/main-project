from flask import*
from database import*
import datetime
import uuid
doctor=Blueprint('doctor',__name__)

@doctor.route('/doctor_home')
def doctor_home():
    data={}
    q="select * from tbl_doctor where username='%s'"%(session['logid'])
    res=select(q)
    print(res)
    name=res[0]['doc_name']
    data['name']=name
	
    return render_template('doctor_home.html',name=name,data=data)

@doctor.route('/doctor_appointment_report',methods=['post','get'])	
def doctor_appointment_report():
   
    data={}
    if "sale" in request.form:
        daily=request.form['daily']
        if request.form['monthly']=="":
            monthly=""
        else:
            monthly=request.form['monthly']+'%'
        print(monthly)
        customer=request.form['customer']	
     
        q="SELECT * ,tbl_appointment.status as status FROM tbl_appointment INNER JOIN tbl_doctor USING(doc_id) inner join tbl_patient using (patient_id) INNER JOIN tbl_payment USING(ap_id)  where  (`rid` like '%s' and p_status='paid' and doc_id='%s' ) or (`adate` like '%s' and p_status='paid' and doc_id='%s' ) or (`adate` like '%s' and p_status='paid' and doc_id='%s' ) order by ap_id DESC "%(customer,session['docid'],daily,session['docid'],monthly,session['docid'])
        res=select(q)
        print(res)
        data['report']=res
        session['res']=res
        r=session['res']
        
    else:
        q="SELECT *,tbl_appointment.status as status FROM tbl_appointment INNER JOIN tbl_doctor USING(doc_id) INNER JOIN tbl_patient USING(patient_id) INNER JOIN tbl_payment USING(ap_id) WHERE p_status='paid' and doc_id='%s' order by adate "%(session['docid'])
        
        res=select(q)
        print(res)
        
        data['report']=res
        session['res']=res
        r=session['res']
        data['len']=len(res)
        # print(data['len'],"..............................")
        
        # dt = "SELECT *,tbl_appointment.status as status FROM tbl_appointment INNER JOIN tbl_doctor USING(doc_id) INNER JOIN tbl_patient USING(patient_id) INNER JOIN tbl_payment USING(ap_id) WHERE p_status='paid' and doc_id='%s' order by adate "%(session['docid']) 
        # appointment_date_str = select(dt)[0]['adate']
        # appointment_date = datetime.datetime.strptime(appointment_date_str, '%Y-%m-%d').date()

        # end_date = appointment_date + datetime.timedelta(days=2)

        # #
        # current_date = datetime.date.today()

        # # Enable the button if the current date is within the appointment date and 2 days after that
        # if appointment_date <= current_date <= end_date:
        #     button_enabled = True
        #     print("hi")
            
        # else:
        #     button_enabled = False
        #     print("hello")
    return render_template('doctor_appointment_report.html',data=data)
 
@doctor.route('/doctor_viewbookings')
def doctor_viewbookings():
    data={}
    pid=request.args['pid']
    q="SELECT *,tbl_appointment.status as status FROM tbl_appointment INNER JOIN tbl_doctor USING(doc_id) INNER JOIN tbl_patient USING(patient_id) INNER JOIN `tbl_payment` USING (ap_id)  where patient_id='%s' and doc_id='%s' and p_status='paid'"%(pid,session['docid'])
    res=select(q)
    data['apppoooo']=res

    
    return render_template('doctor_viewbookings.html',data=data)

@doctor.route('/prescription',methods=['get','post'])
def prescription():
    apid=request.args['apid']
    # con=mysql.connector.connect(user=user,password=password,host="localhost",database=database,port=port)
    # cur=con.cursor(dictionary=True)
    # apid=request.args['apid']
    # # Execute a query to get the appointment date
    q = "SELECT * FROM tbl_appointment WHERE ap_id='%s'" % (apid)
    # appointment_date_str = select(q)[0]['adate']
    # appointment_date = datetime.datetime.strptime(appointment_date_str, '%Y-%m-%d').date()

    # # Calculate the end date as the appointment date plus 2 days
    # end_date = appointment_date + datetime.timedelta(days=2)

    # # Check the current date
    # current_date = datetime.date.today()

    # # Enable the button if the current date is within the appointment date and 2 days after that
    # if appointment_date <= current_date <= end_date:
    #     button_enabled = True
    #     # flash("ok")
    # else:
    #     button_enabled = False
    #     # flash("Not ok")
    data={}
    
    
    # print("......................",button_enabled)

    apid=request.args['apid']

    
    if "pres" in request.form:
        hist=request.form['hist']
        
       
        print("hello")
        q="select * from tbl_appointment where ap_id='%s'"%(apid)
        res=select(q)
        print(q)
        if res:
           
            q1="update tbl_appointment set history='%s' where ap_id='%s'"%(hist,apid)
            update(q1)
            flash("Prescription added")
            return redirect(url_for("doctor.doctor_appointment_report"))            
        else:
            return redirect(url_for("doctor.doctor_appointment_report"))
        
    return render_template('prescription.html',data=data)