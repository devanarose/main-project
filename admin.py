from flask import*
from database import*
import uuid
admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')
@admin.route('/doctor_home')
def doctor_home():
    data={}
    q="select * from tbl_doctor where username='%s'"%(session['logid'])
    res=select(q)
    print(res)
    name=res[0]['doc_name']
    data['name']=name
	
    return render_template('doctor_home.html',name=name,data=data)
@admin.route('/staff_home')
def staff_home():
    data={}
    q="select * from tbl_staff where username='%s'"%(session['logid'])
    res=select(q)
    print(res)
    name=res[0]['staff_fname']+"\t"+res[0]['staff_lname']
    data['name']=name
	
    return render_template('staff_home.html',name=name,data=data)

# @admin.route('/admin_appointment_report')
# def admin_appointment_report():
#     data={}
#     q=" "
#     res=select(q)
#     data['book']=res
#     return render_template('admin_appointment_report.html',data=data)


@admin.route('/cancel_report')
def cancel_report():
    data={}
    q="SELECT * FROM tbl_appointment INNER JOIN tbl_patient USING(patient_id) INNER JOIN `tbl_cancel` USING(ap_id) inner join tbl_doctor using(doc_id)"
    res=select(q)
    data['cancelview']=session['res']
    
    return render_template('cancel_report.html',data=data)



@admin.route('/patient_report')
def patient_report():
    data={}
    q="select * from tbl_patient "
    res=select(q)
    data['patientview']=res
    
    return render_template('patient_report.html',data=data)

@admin.route('/staff_report')
def staff_report():
    data={}
    q="select * from tbl_staff "
    res=select(q)
    data['staffview']=res
    
    return render_template('staff_report.html',data=data)


@admin.route('/doctor_report')
def doctor_report():
    data={}
    q="select * from tbl_doctor "
    res=select(q)
    data['doctorview']=res
    
    return render_template('doctor_report.html',data=data)





@admin.route('/viewpatient',methods=['post','get'])
def viewpatient():
    data={}
    
    if "btn" in request.form:
        search=request.form['search']+'%'
        q="select * from tbl_patient where patient_fname like '%s'"%(search)
        res=select(q)
        
        data['patientview']=res
        print(q)
        
    else:
        q="select * from tbl_patient "
        res=select(q)
        
        data['patientview']=res
       
    
    
    if "action" in request.args:
        action=request.args['action']
        pid=request.args['pid']
        
        if action=='active':
            q="update tbl_patient set status='1' where patient_id='%s'"%(pid)
            update(q)
            return redirect(url_for('admin.viewpatient'))
            
        if action=='inactive':
            q="update tbl_patient set status='0' where patient_id='%s'"%(pid)
            update(q)
            return redirect(url_for('admin.viewpatient'))
        
    return render_template('viewpatient.html',data=data)
@admin.route('/doctor',methods=['post','get'])        
def doctor():
    data={}
    q="select * from tbl_doctor"
    res=select(q)
    data['doctorview']=res
    if "action" in request.args:
        action=request.args['action']
        did=request.args['did']
        
        if action=='active':
            q="update tbl_doctor set doc_status='1' where doc_id='%s'"%(did)
            update(q)
            
            return redirect(url_for('admin.doctor'))
            
        if action=='inactive':
            q="update tbl_doctor set doc_status='0' where doc_id='%s'"%(did)
            update(q)
            return redirect(url_for('admin.doctor'))
        if action=='update':
            q="select * from tbl_doctor where doc_id='%s'"%(did)
            res=select(q)
            data['up']=res
    if "doctor" in request.form:
        e=request.form['email']
        n=request.form['name']
        ddob=request.form['d_dob']
        s=request.form['speci']
        d=request.form['des']
        t1=request.form['st_slot']
        t2=request.form['et_slot']
        f=request.form['fees']
        hn=request.form['hname']
        dis=request.form['District']
        pin=request.form['pincode']
        dg=request.form['doc_gender']
        phone=request.form['phno']
        np=request.form['nop']
        i=request.files['imgg']
        path="static/image"+str(uuid.uuid4())+i.filename
        i.save(path)
        p=request.form['password']
        r="select * from tbl_doctor where username='%s' or doc_phno='%s'"%(e,phone)
        res=select(r)
        if res:
            flash("Doctor already registered")
            return redirect(url_for("admin.doctor"))
        else:
            q="insert into tbl_login values('%s','%s','doctor')"%(e,p)
            insert(q)
            q="INSERT INTO tbl_doctor values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(e,n,ddob,s,d,t1,t2,f,hn,dis,pin,dg,phone,np,path)
            insert(q)
            flash("doctor added")
            return redirect(url_for("admin.doctor"))
    
        
    if "updatedoctor" in request.form:
        n=request.form['name']
        ddob=request.form['d_dob']
        s=request.form['speci']
        d=request.form['des']
        t1=request.form['st_slot']
        t2=request.form['et_slot']
        f=request.form['fees']
        hn=request.form['hname']
        dis=request.form['District']
        pin=request.form['pincode']
        dg=request.form['doc_gender']
        phone=request.form['phno']
        np=request.form['nop']   
        q="update tbl_doctor set doc_name='%s',doc_dob='%s',doc_specialization='%s',description='%s',st_slot='%s',et_slot='%s',fees='%s',doc_hname='%s',doc_district='%s',doc_pin='%s',doc_gender='%s',doc_phno='%s',max_p='%s' where doc_id='%s'"%(n,ddob,s,d,t1,t2,f,hn,dis,pin,dg,phone,np,did)
        update(q)
        flash("Doctor profile updated successfuly")
        return redirect(url_for('admin.doctor'))
    return render_template('doctor.html',data=data)
@admin.route('/staff',methods=['post','get'])
def staff():
    data={}
    q="select * from tbl_staff"
    res=select(q)
    data['staffview']=res
    if "action" in request.args:
        action=request.args['action']
        sid=request.args['sid']
        
        if action=='active':
            q="update tbl_staff set staff_status='1' where staff_id='%s'"%(sid)
            update(q)
            return redirect(url_for('admin.staff'))
            
        if action=='inactive':
            q="update tbl_staff set staff_status='0' where staff_id='%s'"%(sid)
            update(q)
            return redirect(url_for('admin.staff'))
        if action=='update':
            q="select * from tbl_staff where staff_id='%s'"%(sid)
            res=select(q)
            data['up']=res
    if "staff" in request.form:
        e=request.form['email']
        fn=request.form['fname']
        ln=request.form['lname']
        sdob=request.form['staff_dob']
        hno=request.form['staff_hno']
        hn=request.form['hname']
        d=request.form['District']
        pin=request.form['pincode']
        g=request.form['gender']
        phone=request.form['phno']
        p=request.form['password']
        print(e,fn,ln,sdob,hno,hn,d,pin,g,phone,p)
        r="select * from tbl_staff where username='%s' or staff_phno='%s'"%(e,phone)
        res=select(r)
        if res:
            flash("staff already registered")
            return redirect(url_for("admin.staff"))
        else:
            q="insert into tbl_login values('%s','%s','staff')"%(e,p)
            insert(q)
            q="INSERT INTO tbl_staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(e,fn,ln,sdob,hno,hn,d,pin,g,phone)
            insert(q)
            flash("staff added")
            return redirect(url_for('admin.staff'))
        
        
    if "updatestaff" in request.form:
        fn=request.form['fname']
        ln=request.form['lname']
        sdob=request.form['staff_dob']
        hno=request.form['staff_hno']
        hn=request.form['hname']
        d=request.form['District']
        pin=request.form['pincode']
        g=request.form['gender']
        phone=request.form['phno']
        q="update tbl_staff set staff_fname='%s',staff_lname='%s',staff_dob='%s',staff_hno='%s',staff_hname='%s',staff_district='%s',staff_pin='%s',staff_gender='%s',staff_phno='%s' where staff_id='%s'"%(fn,ln,sdob,hno,hn,d,pin,g,phone,sid)
        update(q)
        flash("staff profile updated successfuly")
        return redirect(url_for('admin.staff'))
    return render_template('staff.html',data=data)


@admin.route('/admin_appointment_report',methods=['post','get'])	
def admin_appointment_report():
    data={}
    
    if "sale" in request.form:
        daily=request.form['daily']
        if request.form['monthly']=="":
            monthly=""
        else:
            monthly=request.form['monthly']+'%'
        print(monthly)
        customer=request.form['customer']	
        q="SELECT *,tbl_appointment.status as status FROM tbl_appointment INNER JOIN tbl_doctor USING(doc_id) inner join tbl_patient using(patient_id) INNER JOIN tbl_payment USING(ap_id)  where (`doc_name` like '%s' and tbl_appointment.status <> 'cancelled') or (`adate` like '%s' and tbl_appointment.status <> 'cancelled'  ) or (`adate` like '%s' and tbl_appointment.status <> 'cancelled' )  "%(customer,daily,monthly)
        res=select(q)
        print(q)
        data['report']=res
        session['res']=res
        r=session['res']
    else:
        q="SELECT *,tbl_appointment.status as status FROM tbl_appointment INNER JOIN tbl_doctor USING(doc_id) INNER JOIN tbl_patient USING(patient_id) INNER JOIN tbl_payment USING(ap_id) WHERE tbl_appointment.status <> 'cancelled' order by adate"
        res=select(q)
        data['report']=res
        session['res']=res
        r=session['res']
    if "action" in request.args:
        action=request.args['action']
        apid=request.args['apid']

    else:
        action=None
    
    if action=='report':
        q="update tbl_appointment set report='Not Reported' where ap_id='%s'"%(apid)
        update(q)

        return redirect(url_for('admin.admin_appointment_report'))
    if action=='notreport':
        q="update tbl_appointment set report='Reported' where ap_id='%s'"%(apid)
        update(q)

        return redirect(url_for('admin.admin_appointment_report'))



    return render_template('admin_appointment_report.html',data=data)

@admin.route('/admin_salesreport')
def admin_salesreport():
    data={}
    q="SELECT *,tbl_appointment.status as status FROM tbl_appointment INNER JOIN tbl_doctor USING(doc_id) INNER JOIN tbl_patient USING(patient_id) INNER JOIN tbl_payment USING(ap_id) WHERE p_status='paid'"
    res=select(q)
    data['report']=session['res']
    return render_template('admin_salesreport.html',data=data)	



@admin.route('/admin_cancel_report',methods=['post','get'])
def admin_cancel_report():
    data={}
    if "sale" in request.form:
        daily=request.form['daily']
        if request.form['monthly']=="":
            monthly=""
        else:
            monthly=request.form['monthly']+'%'
        print(monthly)
        customer=request.form['customer']	
        q="SELECT * FROM tbl_appointment inner join tbl_doctor using(doc_id) INNER JOIN tbl_patient USING(patient_id) INNER JOIN `tbl_cancel` USING(ap_id) where (`doc_name` like '%s') or (`adate` like '%s'  ) or (`adate` like '%s' ) "%(customer,daily,monthly)
        res=select(q)
        print(q)
        data['report']=res
        session['res']=res
        r=session['res']
    else:
        q="SELECT * FROM `tbl_appointment`,`tbl_doctor`,`tbl_patient`,`tbl_cancel` WHERE `tbl_appointment`.doc_id=`tbl_doctor`.doc_id AND `tbl_appointment`.patient_id=`tbl_patient`.patient_id AND `tbl_appointment`.`ap_id`=`tbl_cancel`.`ap_id` AND`tbl_appointment`.status='cancelled'"
        res=select(q)
        data['report']=res
        session['res']=res

    return render_template('admin_cancel_report.html',data=data)

@admin.route('/admin_viewbookings')
def admin_viewbookings():
    data={}
    pid=request.args['pid']
    q="SELECT *,tbl_appointment.status as status FROM tbl_appointment INNER JOIN tbl_doctor USING(doc_id) INNER JOIN tbl_patient USING(patient_id) INNER JOIN `tbl_payment` USING (ap_id)  where patient_id='%s' and p_status='paid'"%(pid)
    res=select(q)
    data['apppoooo']=res
    
    return render_template('admin_viewbookings.html',data=data)