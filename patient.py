from flask import *
from database import*


import demjson
from datetime import datetime,timedelta,date


patient=Blueprint('patient',__name__)




@patient.route('/patient_home')
def patient_home():
    q="select * from tbl_patient where patient_id='%s'"%(session['pat_id'])
    res=select(q)
    print(res)
    name=res[0]['patient_fname']+"\t"+res[0]['patient_lname']
    print(name)
	
    return render_template('patient_home.html',name=name)

@patient.route('/cancelhere',methods=['get','post'])
def cancellation():
    data={}
    fees=request.args['fees']
    apid=request.args['apid']
    pid=request.args['pid']
    fees=request.args['fees']
    
    newfee=int(fees)/2
    data['fees']=int(fees)/2
    
    if "can" in request.form:
        
        cname=request.form['card_name']
        bn=request.form['bname']
        bb=request.form['branch']
        an=request.form['acno']
       
        print("hello")
        q="select * from tbl_card where card_name='%s'"%(cname)
        res=select(q)
        print(q)
        if res:
            q="insert into tbl_cancel values(null,'%s','%s','%s','%s','%s','%s')"%(apid,pid,newfee,an,bn,bb)
            insert(q)
            
            q1="update tbl_appointment set status='cancelled' where ap_id='%s'"%(apid)
            update(q1)
            q2="update tbl_payment set p_status='Refund' where p_id='%s'"%(pid)
            update(q2)
            flash("Refund Initiated")
            return redirect(url_for("patient.viewbookings"))
            
        else:
            flash("Incorrect card details")
            return redirect(url_for("patient.patient_home"))
        
    
    return render_template('cancellation.html',data=data)


@patient.route('/bill')
def bill():
    data={}
    apid=request.args['apid']
   
    q="SELECT *,tbl_appointment.status from tbl_appointment inner join tbl_doctor using(doc_id) inner join tbl_patient using(patient_id) where ap_id='%s' "%(apid)
    res=select(q)
    print(q)
    data['book']=res
    return render_template('bill.html',data=data)

@patient.route('/appointment_report')
def appointment_report():
    data={}
    q="SELECT * from tbl_appointment inner join tbl_doctor using(doc_id) inner join tbl_patient using(patient_id) where  patient_id='%s' "%(session['pat_id'])
    res=select(q)
    data['book']=res
    return render_template('appointment_report.html',data=data)

@patient.route('/newpayment',methods=['post','get'])
def newpayment():
    data={}
    aid=request.args['aid']
    q="select * from tbl_card"
    res=select(q)
    data['pay']=res
    
    
    if "btnnss" in request.form:
        cno=request.form['card_no']
        cname=request.form['card_name']
        exp=request.form['exp_date']
        
       
        
        q="select * from tbl_card"
        res=select(q)
        if res:
            q="INSERT INTO tbl_card values(null,'%s','%s','%s','%s')"%(session['pat_id'],cno,cname,exp)
            insert(q)
            print(q)
            q="insert into tbl_payment values(null,'%s','%s','paid')"%(aid,date.today())
            insert(q)
            print(q)
            q="UPDATE tbl_appointment INNER JOIN tbl_payment USING(ap_id) SET status='booked' WHERE p_status='paid'"
            update(q)
            print(q)
            flash("Payment successful")
            return redirect(url_for('patient.viewbookings'))
       
    
    return render_template('newpayment.html',data=data)

@patient.route('/updatepatient',methods=['post','get'])
def updatepatient():
    data={}
    q="select * from tbl_patient where username='%s'"%(session['logid'])
    res=select(q)
    data['patientview']=res
    
    if "patient" in request.form:
        fn=request.form['fname']
        ln=request.form['lname']
        pdob=request.form['p_dob']
        pg=request.form['pgender']
        hn=request.form['hname']
        d=request.form['District']
        pin=request.form['pincode']
        phone=request.form['phno']
        
        print(fn,ln,pdob,pg,hn,d,pin,phone)
        q="update tbl_patient set patient_fname='%s', patient_lname='%s', p_dob='%s', p_gender='%s',patient_hname='%s',patient_district='%s',patient_pin='%s',patient_phno='%s' where patient_id='%s'"%(fn,ln,pdob,pg,hn,d,pin,phone,session['pat_id'])
        update(q)
        flash("Profile updated successfuly")
        return redirect(url_for('patient.updatepatient'))
    return render_template('updatepatient.html',data=data)

@patient.route('/appointment',methods=['post','get'])
def appointment():
    data={}

    q="SELECT *,concat(doc_name,', ',doc_specialization) as dot FROM `tbl_doctor` where doc_status=1 "
    # q="select * from tbl_doctor"
    res=select(q)
    
    
    if res:
        data['appoin']=res
        
        x = res[0]['st_slot']
        y = res[0]['et_slot']
        hour_and_minute=x
        date_time_obj = datetime.strptime(x, '%H:%M')
        print (date_time_obj)
        s=[]
        while hour_and_minute<y:
            if hour_and_minute<y:
                date_time_obj += timedelta(minutes=5)
                hour_and_minute = date_time_obj.strftime("%H:%M")
                print(hour_and_minute)
                s.append(hour_and_minute)
            else:
                break
        data['s']=s
        
        
    if "booknow" in request.form:
        t=request.form['t_box']
        apdate=request.form['adate']
        
       
        
        department=request.form['department']
        q1="select * from tbl_doctor where doc_id='%s'"%(department)
        ress=select(q1)
        doc_fee=ress[0]['fees']
        
        c="SELECT * FROM `tbl_appointment` WHERE `adate`='%s' and status='booked' AND `patient_id`='%s'"%(apdate,session['pat_id'])  
        check=select(c)
        
       
        
        q="SELECT * FROM `tbl_appointment` WHERE `adate`='%s' and status='booked' AND `doc_id`='%s' AND `patient_id`='%s'"%(apdate,department,session['pat_id'])
        exist=select(q)
        
        if check:
            flash("You can only have an appointment booked on this date")
        else:
            q2="INSERT INTO tbl_appointment values(null,'%s','%s','%s','%s','%s','Not Booked',curdate(),'pending','not prescribed')"%(session['pat_id'],department,t,apdate,doc_fee)
            aid=insert(q2)
            return redirect(url_for("patient.newpayment",aid=aid))
        
    return render_template('appointment.html',data=data)


@patient.route('/viewbookings')
def viewbookings():
    data={}
    half=""
    fees=""
    new_date=""
    today=""
    
    q="SELECT *,tbl_appointment.status as status FROM tbl_appointment INNER JOIN tbl_doctor USING(doc_id) INNER JOIN tbl_patient USING(patient_id) INNER JOIN `tbl_payment` USING (ap_id) where patient_id='%s'"%(session['pat_id'])
    res=select(q)
    print(q)
    data['book']=res
    # from datetime import date
    # today = date.today()
 

    # <td><a style="width: 150px" class="btn btn-info" href="cancelhere?apid={{row['ap_id']}}&pid={{row['p_id']}}&fees={{ row['fees'] }}"><b>Cancel</b></a></td>
		
    if "action" in request.args:
        action=request.args['action']
        aid=request.args['apid']
        fees=request.args['fees']
        pid=request.args['pid']
        
    else:
        action=None
        
    if action=='cancel':
        
        from datetime import datetime, timedelta
        
        q="select * from tbl_appointment where ap_id='%s'"%(aid)
        starting_date=select(q)[0]['booking_date']
        print(type(starting_date))
        today = date.today()
     
        starting_date = datetime.strptime(starting_date, '%Y-%m-%d')
        # Add 3 days to the initial date
        new_date = starting_date + timedelta(days=3)
        
        current_date = datetime.now()
        print(".............",new_date)
        print(".............",current_date)
        if current_date > new_date:
            flash("Cancel Period is Over!")
        else:
            return redirect(url_for("patient.cancellation",apid=aid,pid=pid,fees=fees))
            # q2="insert into tbl_cancel values(null,'%s','%s','%s')"%(aid,pid,fees)
            # insert(q2)
            # q="update tbl_appointment set status='cancelled' where ap_id='%s'"%(aid)
            # update(q)
            # half=int(fees)*0.5
    return render_template('viewbookings.html',data=data,half=half,fees=fees,new_date=new_date,today=today)


from datetime import datetime
@patient.route('/select_timeslot',methods=['get','post'])
def select_timeslot():
    data={}
    form_data = request.get_json()
    select_cound = form_data['selected']
    date = form_data['date']
    
    print("id........................",date)
    q="select * from tbl_doctor where doc_id='%s'"%(select_cound)
    res=select(q)
    if res:
        data['appoin']=res
        maxP = res[0]['max_p']
        
        x = res[0]['st_slot']
        y = res[0]['et_slot']
        hour_and_minute=x
        
        newx = x[0:2]
        newy = y[0:2]
        
        diff = int(newy) - int(newx)
        print("////////////",diff)
        val = 0
        if diff == 1:
            val=60
        elif diff == 2:
            val=120
        elif diff == 3:
            val=180
   
   
      
        date_time_obj = datetime.strptime(x, '%H:%M')
        s=[]
        while hour_and_minute<y:
            if hour_and_minute<y:
                date_time_obj += timedelta(minutes=(val/maxP))
                hour_and_minute = date_time_obj.strftime("%H:%M")
                # print(hour_and_minute)
                q="SELECT * FROM `tbl_appointment` WHERE doc_id='%s' AND adate='%s' and t_box='%s' and status <> 'cancelled' " %(select_cound,date,hour_and_minute)
                res=select(q)
                if not res:
                    s.append(hour_and_minute)
            else:
                break
        data['s']=s
        print(data['s'])
    
    
    return demjson.encode(data['s'])
