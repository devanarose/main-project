from flask import*
from database import*
import uuid
staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staff_home():
    return render_template('staff_home.html')
@staff.route('/staff_doc')
def staff_doc():
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
            return redirect(url_for('staff.staff_doc'))
            
        if action=='inactive':
            q="update tbl_doctor set doc_status='0' where doc_id='%s'"%(did)
            update(q)
            return redirect(url_for('staff.staff_doc'))
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
                q="insert into tbl_login values('%s','%s','doctor')"%(e,p)
                insert(q)
                q="INSERT INTO tbl_doctor values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(e,n,ddob,s,d,t1,t2,f,hn,dis,pin,dg,phone,np,path)
                insert(q)
                flash("doctor added")
                return redirect(url_for('staff.staff_doc'))
        
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
        flash("doctor profile updated")
        return redirect(url_for('staff.staff_doc'))
    return render_template('staff_doc.html',data=data)
@staff.route('/staff_patient',methods=['get','post'])
def staff_patient():
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
            return redirect(url_for('staff.staff_patient'))
            
        if action=='inactive':
            q="update tbl_patient set status='0' where patient_id='%s'"%(pid)
            update(q)
            return redirect(url_for('staff.staff_patient'))
        
    return render_template('staff_patient.html',data=data)
@staff.route('/staff_appointment_report',methods=['post','get'])	
def staff_appointment_report():
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
        q="SELECT *,tbl_appointment.status as status FROM tbl_appointment INNER JOIN tbl_doctor USING(doc_id) INNER JOIN tbl_patient USING(patient_id) INNER JOIN tbl_payment USING(ap_id) WHERE p_status='paid' order by adate"
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

        return redirect(url_for('staff.staff_appointment_report'))
    if action=='notreport':
        q="update tbl_appointment set report='Reported' where ap_id='%s'"%(apid)
        update(q)

        return redirect(url_for('staff.staff_appointment_report'))
    return render_template('staff_appointment_report.html',data=data)

@staff.route('/staff_cancel_report',methods=['post','get'])
def staff_cancel_report():
    data={}
    if "sale" in request.form:
        daily=request.form['daily']
        if request.form['monthly']=="":
            monthly=""
        else:
            monthly=request.form['monthly']+'%'
        print(monthly)
        customer=request.form['customer']	
        q="SELECT * FROM tbl_appointment inner join tbl_doctor using(doc_id) INNER JOIN tbl_patient USING(patient_id) INNER JOIN `tbl_cancel` USING(ap_id) where (`doc_name` like '%s') or (`adate` like '%s'  ) or (`adate` like '%s' )"%(customer,daily,monthly)
        res=select(q)
        print(q)
        data['report']=res
        session['res']=res
        r=session['res']
    else:
        q="SELECT * FROM tbl_appointment INNER JOIN tbl_patient USING(patient_id) INNER JOIN `tbl_cancel` USING(ap_id) inner join tbl_doctor using(doc_id)"
        res=select(q)
        data['report']=res
        session['res']=res
    return render_template('staff_cancel_report.html',data=data)

@staff.route('/staff_viewbookings')
def staff_viewbookings():
    data={}
    pid=request.args['pid']
    q="SELECT *,tbl_appointment.status as status FROM tbl_appointment INNER JOIN tbl_doctor USING(doc_id) INNER JOIN tbl_patient USING(patient_id) INNER JOIN `tbl_payment` USING (ap_id)  where patient_id='%s' and p_status='paid'"%(pid)
    res=select(q)
    data['apppoooo']=res
    
    return render_template('staff_viewbookings.html',data=data)