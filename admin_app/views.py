from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

import mysql.connector as mcdb

conn = mcdb.connect(host="localhost", user="root", passwd="", database='crm2')
print('Successfully connected to database')


cur = conn.cursor()
    # Data insert,display,delete in mysql xampp...

def country(request):
    return render(request,'country.html')

def country_added(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['name']
        cur.execute("INSERT INTO  country_tbl (country_name) VALUES ('{}')".format(catname))
        conn.commit()
        messages.info(request, 'Data Submitted Successfully')
        return redirect(country) 
    else:
        return redirect(country)
    
def countrytable(request):
    cur.execute("SELECT * FROM `country_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'countrytable.html',{'mydata': data})

def countryedit(request,id):
    cur.execute("SELECT * FROM `country_tbl` where country_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request,'countryedit.html',{'mydata': data})

def country_update(request):
    if request.method == 'POST':
        print(request.POST)
        cid = request.POST['txt1']
        catname = request.POST['name']
        cur.execute("update  `country_tbl` set `country_name` = '{}' where  `country_id` = '{}' ".format(catname,cid))
        conn.commit()
        messages.info(request, 'Data Updated Successfully')
        return redirect(country) 
    else:
        return redirect(country)

def countrydelete(request,id):
    print(id)
    cur.execute("delete from `country_tbl` where `country_id` = {}".format(id))
    conn.commit()
    messages.info(request, 'Data Deleted Successfully')
    return redirect(countrytable) 



def state(request):
    cur.execute("SELECT * FROM `country_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'state.html',{'mydata': data})

def state_added(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['name']
        catstateid = request.POST['id']
        cur.execute("INSERT INTO  state_tbl (state_name,country_id) VALUES ('{}','{}')".format(catname,catstateid))
        conn.commit()
        messages.info(request, 'Data Submitted Successfully')
        return redirect(state) 
    else:
        return redirect(state)

def statetable(request):
    cur.execute('''SELECT
    `state_tbl`.`state_id`
    , `state_tbl`.`state_name`
    , `country_tbl`.`country_name`
FROM
    `country_tbl`
    INNER JOIN `state_tbl` 
        ON (`country_tbl`.`country_id` = `state_tbl`.`country_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'statetable.html',{'mydata': data})

def stateedit(request,id):
    cur.execute("SELECT * FROM `state_tbl` where state_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request,'stateedit.html',{'mydata': data})

def state_update(request):
    if request.method == 'POST':
        print(request.POST)
        sid = request.POST['txt1']
        catsname = request.POST['name']
        cur.execute("update  `state_tbl` set `state_name` = '{}' where  `state_id` = '{}' ".format(catsname,sid))
        conn.commit()
        messages.info(request, 'Data Updated Successfully')
        return redirect(state) 
    else:
        return redirect(state)

def statedelete(request,id):
    print(id)
    cur.execute("delete from `state_tbl` where `state_id` = {}".format(id))
    conn.commit()
    messages.info(request, 'Data Deleted Successfully')
    return redirect(statetable)



def city(request):
    cur.execute("select * FROM `state_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'city.html',{'mydata': data})

def city_added(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['name']
        catcityid = request.POST['id']
        cur.execute("INSERT INTO city_tbl(city_name, state_id) VALUES  ('{}','{}')".format(catname,catcityid))
        conn.commit()
        messages.info(request, 'Data Submitted Successfully')
        return redirect(city) 
    else:
        return redirect(city)
    
def citytable(request):
    cur.execute('''SELECT
    `city_tbl`.`city_id`
    , `city_tbl`.`city_name`
    , `state_tbl`.`state_name`
FROM
    `state_tbl`
    INNER JOIN `city_tbl` 
        ON (`state_tbl`.`state_id` = `city_tbl`.`state_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'citytable.html',{'mydata': data})    

def cityedit(request,id):
    cur.execute("SELECT * FROM `city_tbl` where city_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request,'cityedit.html',{'mydata': data})

def city_update(request):
    if request.method == 'POST':
        print(request.POST)
        cid = request.POST['txt1']
        catname = request.POST['name']
        cur.execute("update  `city_tbl` set `city_name` = '{}' where  `city_id` = '{}' ".format(catname,cid))
        conn.commit()
        messages.info(request, 'Data Updated Successfully')
        return redirect(city) 
    else:
        return redirect(city)

def citydelete(request,id):
    print(id)
    cur.execute("delete from `city_tbl` where `city_id` = {}".format(id))
    conn.commit()
    messages.info(request, 'Data Deleted Successfully')
    return redirect(citytable)



def program(request):
    cur.execute("SELECT * FROM `student_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'program.html',{'mydata': data})

def program_added(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['name']
        catcode = request.POST['code']
        catminduration = request.POST['minduration']
        catmaxduration = request.POST['maxduration']
        catid = request.POST['id']
        cur.execute("INSERT INTO program_tbl (program_name, program_code, minduration, maxduration, student_id) VALUES ('{}','{}','{}','{}','{}')".format(catname,catcode,catminduration,catmaxduration,catid))
        conn.commit()
        messages.info(request, 'Data Submitted Successfully')
        return redirect(program) 
    else:
        return redirect(program)
    
def programtable(request):
    cur.execute('''SELECT
    `program_tbl`.`program_id`
    , `program_tbl`.`program_name`
    , `program_tbl`.`program_code`
    , `program_tbl`.`minduration`
    , `program_tbl`.`maxduration`
    , `user_tbl`.`first_name`
    , `user_tbl`.`middle_name`
    , `user_tbl`.`last_name`
FROM
    `student_tbl`
    INNER JOIN `program_tbl` 
        ON (`student_tbl`.`student_id` = `program_tbl`.`student_id`)
    INNER JOIN `user_tbl` 
        ON (`user_tbl`.`userid` = `student_tbl`.`user_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'programtable.html',{'mydata': data})

def programedit(request,id):
    cur.execute("SELECT * FROM `program_tbl` where program_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `student_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request,'programedit.html',{'mydata': data,'mydata1': data1})

def program_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catname = request.POST['name']
        catcode = request.POST['code']
        catminduration = request.POST['minduration']
        catmaxduration = request.POST['maxduration']
        catsid = request.POST['id']
        cur.execute("UPDATE `program_tbl` SET `program_name`= '{}',`program_code`= '{}' , `minduration`= '{}' , `maxduration`= '{}' , `student_id`= '{}' WHERE  `program_id`= '{}'".format(catname,catcode,catminduration,catmaxduration,catsid,catid))
        conn.commit()
        messages.info(request, 'Data Updated Successfully')
        return redirect(program) 
    else:
        return redirect(program)

def programdelete(request,id):
    print(id)
    cur.execute("delete from `program_tbl` where `program_id` = {}".format(id))
    conn.commit()
    messages.info(request, 'Data Deleted Successfully')
    return redirect(programtable)



def semester(request):
    cur.execute("SELECT * FROM `program_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'semester.html',{'mydata': data,'mydata2': data2})

def semester_added(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['name']
        catpid = request.POST['programid']
        catfid = request.POST['facultyid']
        cur.execute("INSERT INTO  semester_tbl (semester_name, program_id, faculty_id) VALUES ('{}','{}','{}')".format(catname,catpid,catfid))
        conn.commit()
        messages.info(request, 'Data Submitted Successfully')
        return redirect(semester) 
    else:
        return redirect(semester)
    
def semestertable(request):
    cur.execute('''SELECT
    `semester_tbl`.`semester_id`
    , `semester_tbl`.`semester_name`
    , `program_tbl`.`program_name`
    , `faculty_tbl`.`faculty_name`
FROM
    `program_tbl`
    INNER JOIN `semester_tbl` 
        ON (`program_tbl`.`program_id` = `semester_tbl`.`program_id`)
    INNER JOIN `faculty_tbl` 
        ON (`faculty_tbl`.`faculty_id` = `semester_tbl`.`faculty_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'semestertable.html',{'mydata': data})

def semesteredit(request,id):
    cur.execute("SELECT * FROM `semester_tbl` where semester_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `program_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'semesteredit.html',{'mydata': data,'mydata1': data1,'mydata2': data2})

def semester_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catname = request.POST['name']
        catpid = request.POST['programid']
        catfid = request.POST['facultyid']
        cur.execute("UPDATE `semester_tbl` SET `semester_name`= '{}',`program_id`= '{}',`faculty_id`= '{}' WHERE semester_id = '{}'".format(catname,catpid,catfid,catid))
        conn.commit()
        messages.info(request, 'Data Updated Successfully')
        return redirect(semester) 
    else:
        return redirect(semester)

def semesterdelete(request,id):
    print(id)
    cur.execute("delete from `semester_tbl` where `semester_id` = {}".format(id))
    conn.commit()
    messages.info(request, 'Data Deleted Successfully')
    return redirect(semestertable)



def user(request):
    cur.execute("SELECT * FROM `city_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `state_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    cur.execute("SELECT * FROM `country_tbl`")
    data3 = cur.fetchall()
    #return list(data)
    print(list(data3))
    return render(request,'user.html',{'mydata': data,'mydata2': data2,'mydata3': data3})

def user_added(request):
    if request.method == 'POST':
        print(request.POST)
        catfname = request.POST['fname']
        catmname = request.POST['mname']
        catlname = request.POST['lname']
        catdob = request.POST['dob']
        catgender = request.POST['gender']
        catuemail = request.POST['uemail']
        cataemail = request.POST['aemail']
        catcontact = request.POST['contact']
        catacontact = request.POST['acontact']
        catpaddressline1 = request.POST['paddressline1']
        catpaddressline2 = request.POST['paddressline2']
        catplandmarkroad = request.POST['plandmarkroad']
        catppincode = request.POST['ppincode']
        catpid = request.POST['pid']
        catsid = request.POST['sid']
        catpcid = request.POST['pcid']
        catcaddressline1 = request.POST['caddressline1']
        catcaddressline2 = request.POST['caddressline2']
        catclandmarkroad = request.POST['clandmarkroad']
        catcpincode = request.POST['cpincode']
        catcid = request.POST['cid']
        catcsid=request.POST['csid']
        catccid=request.POST['ccid']
        catpassword = request.POST['password']
        catusertype = request.POST['usertype']

        #Mail Send Code thai gayu 
        subject = 'New Account Created'
        message = ' Hello User Your New Account created in  CRM  Email Id is' + catuemail +' Your Password is  ' + catpassword
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [catuemail]
        send_mail( subject, message, email_from, recipient_list )
        cur.execute("INSERT INTO `user_tbl`(`first_name`, `middle_name`, `last_name`, `date_of_birth`, `gender`, `uemail`, `aemail`, `contact`, `altcontact`, `paddressline1`, `paddressline2`, `plandmarkroad`, `ppincode`, `pcity_id`,`pstate_id`,`pcountry_id`, `caddressline1`, `caddressline2`, `clandmarkroad`, `cpincode`, `ccity_id`,`cstate_id`,`ccountry_id`, `password`, `usertype`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(catfname,catmname,catlname,catdob,catgender,catuemail,cataemail,catcontact,catacontact,catpaddressline1,catpaddressline2,catplandmarkroad,catppincode,catpid,catsid,catpcid,catcaddressline1,catcaddressline2,catclandmarkroad,catcpincode,catcid,catcsid,catccid,catpassword,catusertype))
        conn.commit()
        messages.info(request, 'Data Submitted Successfully')
        return redirect(user) 
    else:
        return redirect(user)

def usertable(request):
    cur.execute('''SELECT
    `user_tbl`.`userid`
    , `user_tbl`.`first_name`
    , `user_tbl`.`middle_name`
    , `user_tbl`.`last_name`
    , `user_tbl`.`date_of_birth`
    , `user_tbl`.`gender`
    , `user_tbl`.`uemail`
    , `user_tbl`.`aemail`
    , `user_tbl`.`contact`
    , `user_tbl`.`altcontact`
    , `user_tbl`.`paddressline1`
    , `user_tbl`.`paddressline2`
    , `user_tbl`.`plandmarkroad`
    , `user_tbl`.`ppincode`
    , `city_tbl`.`city_name`
    , `state_tbl`.`state_name`
    , `country_tbl`.`country_name`
    , `user_tbl`.`caddressline1`
    , `user_tbl`.`caddressline2`
    , `user_tbl`.`clandmarkroad`
    , `user_tbl`.`cpincode`
    , `city_tbl`.`city_name`
    , `state_tbl`.`state_name`
    , `country_tbl`.`country_name`
    , `user_tbl`.`password`
    , `user_tbl`.`usertype`
FROM
    `city_tbl`
    INNER JOIN `user_tbl` 
        ON (`city_tbl`.`city_id` = `user_tbl`.`pcity_id`) AND (`city_tbl`.`city_id` = `user_tbl`.`ccity_id`)
    INNER JOIN `country_tbl` 
        ON (`country_tbl`.`country_id` = `user_tbl`.`pcountry_id`) AND (`country_tbl`.`country_id` = `user_tbl`.`ccountry_id`)
    INNER JOIN `state_tbl` 
        ON (`state_tbl`.`state_id` = `user_tbl`.`pstate_id`) AND (`state_tbl`.`state_id` = `user_tbl`.`cstate_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'usertable.html',{'mydata': data})   

def useredit(request,id):
    cur.execute("SELECT * FROM `user_tbl` where userid = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `city_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))  
    cur.execute("SELECT * FROM `state_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    cur.execute("SELECT * FROM `country_tbl`")
    data3 = cur.fetchall()
    #return list(data)
    print(list(data3))
    return render(request,'useredit.html',{'mydata': data,'mydata1': data1,'mydata2': data2,'mydata3': data3})

def user_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catfname = request.POST['fname']
        catmname = request.POST['mname']
        catlname = request.POST['lname']
        catdob = request.POST['dob']
        catgender = request.POST['gender']
        catuemail = request.POST['uemail']
        cataemail = request.POST['aemail']
        catcontact = request.POST['contact']
        catacontact = request.POST['acontact']
        catpaddressline1 = request.POST['paddressline1']
        catpaddressline2 = request.POST['paddressline2']
        catplandmarkroad = request.POST['plandmarkroad']
        catppincode = request.POST['ppincode']
        catpid = request.POST['pid']
        catsid= request.POST['sid']
        catpcid = request.POST['pcid']
        catcaddressline1 = request.POST['caddressline1']
        catcaddressline2 = request.POST['caddressline2']
        catclandmarkroad = request.POST['clandmarkroad']
        catcpincode = request.POST['cpincode']
        catcid = request.POST['cid']
        catcsid = request.POST['csid']
        catccid= request.POST['ccid']
        catpassword = request.POST['password']
        catusertype = request.POST['usertype']
        cur.execute("UPDATE `user_tbl` SET `first_name`= '{}' , `middle_name`= '{}' , `last_name`= '{}' , `date_of_birth`= '{}' , `gender`= '{}' , `uemail`= '{}' , `aemail`= '{}' , `contact`= '{}',`altcontact`= '{}' , `paddressline1`= '{}' , `paddressline2`= '{}' , `plandmarkroad`= '{}' , `ppincode`= '{}' , `pcity_id`= '{}',`pstate_id`='{}',`pcountry_id`='{}' , `caddressline1`= '{}' , `caddressline2`= '{}' , `clandmarkroad`= '{}' , `cpincode`= '{}' , `ccity_id`= '{}',`cstate_id`='{}' , `ccountry_id`= '{}', `password`= '{}' , `usertype`= '{}' WHERE `userid` = '{}'".format(catfname,catmname,catlname,catdob,catgender,catuemail,cataemail,catcontact,catacontact,catpaddressline1,catpaddressline2,catplandmarkroad,catppincode,catpid,catsid,catpcid,catcaddressline1,catcaddressline2,catclandmarkroad,catcpincode,catcid,catcsid,catccid,catpassword,catusertype,catid))
        conn.commit()
        messages.info(request, 'Data Updated Successfully')
        return redirect(user) 
    else:
        return redirect(user)

def userdelete(request,id):
    print(id)
    cur.execute("delete from `user_tbl` where `userid` = {}".format(id))
    conn.commit()
    messages.info(request, 'Data Deleted Successfully')
    return redirect(usertable)



def studentform(request):
    cur.execute("SELECT * FROM `user_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'studentform.html',{'mydata': data})

def student_added(request):
    if request.method == 'POST':
        print(request.POST)
        catuid = request.POST['uid']
        catno = request.POST['no']
        catdate = request.POST['date']
        catyear = request.POST['year']
        catvalidupto = request.POST['validupto']
        catregional = request.POST['regional']
        catstudycenter = request.POST['studeycenter']
        catmedium = request.POST['medium']
        cur.execute("INSERT INTO `student_tbl`(`user_id`,`enrollment_no`, `enrollment_date`, `admission_year`, `addmissionvalidupto`, `regionalcenter`, `studentstudycenter`, `medium`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(catuid,catno,catdate,catyear,catvalidupto,catregional,catstudycenter,catmedium))
        conn.commit()
        return redirect(studentform) 
    else:
        return redirect(studentform)

def studenttable(request):
    cur.execute('''SELECT
    `student_tbl`.`student_id`
    , `user_tbl`.`first_name`
    , `user_tbl`.`middle_name`
    , `user_tbl`.`last_name`
    , `student_tbl`.`enrollment_no`
    , `student_tbl`.`enrollment_date`
    , `student_tbl`.`admission_year`
    , `student_tbl`.`addmissionvalidupto`
    , `student_tbl`.`regionalcenter`
    , `student_tbl`.`studentstudycenter`
    , `student_tbl`.`medium`
FROM
    `user_tbl`
    INNER JOIN `student_tbl` 
        ON (`user_tbl`.`userid` = `student_tbl`.`user_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'studenttable.html',{'mydata': data})

def studentformedit(request,id):
    cur.execute("SELECT * FROM `student_tbl` where student_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `user_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request,'studentformedit.html',{'mydata': data,'mydata1': data1})

def student_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catno = request.POST['no']
        catdate = request.POST['date']
        catyear = request.POST['year']
        catvalidupto = request.POST['validupto']
        catregional = request.POST['regional']
        catstudycenter = request.POST['studeycenter']
        catmedium = request.POST['medium']
        cur.execute("UPDATE `student_tbl` SET `user_id`='{}',`enrollment_no`='{}',`enrollment_date`='{}',`admission_year`='{}',`addmissionvalidupto`='{}',`regionalcenter`='{}',`studentstudycenter`='{}',`medium`='{}' WHERE 1 student_id = '{}'".format(catno,catdate,catyear,catvalidupto,catregional,catstudycenter,catmedium,catid))
        conn.commit()
        return redirect(studentform) 
    else:
        return redirect(studentform)


def studentdelete(request,id):
    print(id)
    cur.execute("delete from `student_tbl` where `student_id` = {}".format(id))
    conn.commit()
    return redirect(studenttable)



def facultyform(request):
    cur.execute("SELECT * FROM `user_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `program_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'facultyform.html',{'mydata': data,'mydata2': data2})

def faculty_added(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['name']
        catqulification = request.POST['qulification']
        catuid = request.POST['uid']
        catpid = request.POST['pid']
        cur.execute("INSERT INTO `faculty_tbl`(`faculty_name`, `faculty_qulification`, `user_id`, `program_id`) VALUES  ('{}','{}','{}','{}')".format(catname,catqulification,catuid,catpid))
        conn.commit()
        return redirect(facultyform) 
    else:
        return redirect(facultyform)

def facultytable(request):
    cur.execute('''SELECT
    `faculty_tbl`.`faculty_id`
    , `faculty_tbl`.`faculty_name`
    , `faculty_tbl`.`faculty_qulification`
    , `user_tbl`.`first_name`
    , `user_tbl`.`middle_name`
    , `user_tbl`.`last_name`
    , `program_tbl`.`program_name`
FROM
    `user_tbl`
    INNER JOIN `faculty_tbl` 
        ON (`user_tbl`.`userid` = `faculty_tbl`.`user_id`)
    INNER JOIN `program_tbl` 
        ON (`program_tbl`.`program_id` = `faculty_tbl`.`program_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'facultytable.html',{'mydata': data})

def facultyformedit(request,id):
    cur.execute("SELECT * FROM `faculty_tbl` where faculty_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `user_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    cur.execute("SELECT * FROM `program_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'facultyformedit.html',{'mydata': data,'mydata1': data1,'mydata2': data2})

def faculty_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catname = request.POST['name']
        catqulification = request.POST['qulification']
        catuid = request.POST['uid']
        catpid = request.POST['pid']
        cur.execute("UPDATE `faculty_tbl` SET `faculty_name`= '{}',`faculty_qulification`= '{}',`user_id`= '{}',`program_id`= '{}' WHERE  faculty_id = '{}'".format(catname,catqulification,catuid,catpid,catid))
        conn.commit()
        return redirect(facultyform) 
    else:
        return redirect(facultyform)

def facultydelete(request,id):
    print(id)
    cur.execute("delete from `faculty_tbl` where `faculty_id` = {}".format(id))
    conn.commit()
    return redirect(facultytable)



def coursecategory(request):
    return render(request,'coursecategory.html')

def coursecategory_added(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['name']
        cur.execute("INSERT INTO `coursecategory_tbl`( `coursecategory_name`)  VALUES ('{}')".format(catname))
        conn.commit()
        return redirect(coursecategory) 
    else:
        return redirect(coursecategory)

def coursecategorytable(request):
    cur.execute("SELECT * FROM `coursecategory_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'coursecategorytable.html',{'mydata': data})

def coursecategoryedit(request,id):
    cur.execute("SELECT * FROM `coursecategory_tbl` where coursecategory_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request,'coursecategoryedit.html',{'mydata': data})

def coursecategory_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catname = request.POST['name']
        cur.execute("UPDATE `coursecategory_tbl` SET `coursecategory_name`= '{}' WHERE coursecategory_id = '{}'".format(catname,catid))
        conn.commit()
        return redirect(coursecategory) 
    else:
        return redirect(coursecategory)


def coursecategorydelete(request,id):
    print(id)
    cur.execute("delete from `coursecategory_tbl` where `coursecategory_id` = {}".format(id))
    conn.commit()
    return redirect(coursecategorytable)



def coursetype(request):
    return render(request,'coursetype.html')

def coursetype_added(request):
    if request.method == 'POST':
        print(request.POST)
        cattype = request.POST['type']
        cur.execute("INSERT INTO `coursetype_tbl`(`coursetype`)  VALUES ('{}')".format(cattype))
        conn.commit()
        return redirect(coursetype) 
    else:
        return redirect(coursetype)

def coursetypetable(request):
    cur.execute("SELECT * FROM `coursetype_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'coursetypetable.html',{'mydata': data})

def coursetypeedit(request,id):
    cur.execute("SELECT * FROM `coursetype_tbl` where coursetype_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request,'coursetypeedit.html',{'mydata': data})

def coursetype_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        cattype = request.POST['type']
        cur.execute("UPDATE `coursetype_tbl` SET `coursetype`= '{}' WHERE  coursetype_id = '{}'".format(cattype,catid))
        conn.commit()
        return redirect(coursetype) 
    else:
        return redirect(coursetype)

def coursetypedelete(request,id):
    print(id)
    cur.execute("delete from `coursetype_tbl` where `coursetype_id` = {}".format(id))
    conn.commit()
    return redirect(coursetypetable)



def course(request):
    cur.execute("SELECT * FROM `coursecategory_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `coursetype_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    cur.execute("SELECT * FROM `program_tbl`")
    data3 = cur.fetchall()
    #return list(data)
    print(list(data3))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data4 = cur.fetchall()
    #return list(data)
    print(list(data4))
    return render(request,'course.html',{'mydata': data,'mydata2':data2,'mydata3':data3,'mydata4':data4})

def course_added(request):
    if request.method == 'POST':
        print(request.POST)
        catcode = request.POST['code']
        catname = request.POST['name']
        catmaxmarks = request.POST['maxmarks']
        catminmarks = request.POST['minmarks']
        catcid = request.POST['cid']
        catcid1 = request.POST['cid1']
        catpid = request.POST['pid']
        catfid = request.POST['fid']
        cur.execute("INSERT INTO `course_tbl`(`course_code`, `course_name`, `course_maxmarks`, `course_minmarks`, `coursecategory_id`, `coursetype_id`, `program_id`, `faculty_id`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(catcode,catname,catmaxmarks,catminmarks,catcid,catcid1,catpid,catfid))
        conn.commit()
        return redirect(course) 
    else:
        return redirect(course)

def coursetable(request):
    cur.execute('''SELECT
    `course_tbl`.`course_id`
    , `course_tbl`.`course_code`
    , `course_tbl`.`course_name`
    , `course_tbl`.`course_maxmarks`
    , `course_tbl`.`course_minmarks`
    , `coursecategory_tbl`.`coursecategory_name`
    , `coursetype_tbl`.`coursetype`
    , `program_tbl`.`program_name`
    , `faculty_tbl`.`faculty_name`
FROM
    `coursecategory_tbl`
    INNER JOIN `course_tbl` 
        ON (`coursecategory_tbl`.`coursecategory_id` = `course_tbl`.`coursecategory_id`)
    INNER JOIN `coursetype_tbl` 
        ON (`coursetype_tbl`.`coursetype_id` = `course_tbl`.`coursetype_id`)
    INNER JOIN `program_tbl` 
        ON (`program_tbl`.`program_id` = `course_tbl`.`program_id`)
    INNER JOIN `faculty_tbl` 
        ON (`faculty_tbl`.`faculty_id` = `course_tbl`.`faculty_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'coursetable.html',{'mydata': data})

def courseedit(request,id):
    cur.execute("SELECT * FROM `course_tbl` where course_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `coursecategory_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    cur.execute("SELECT * FROM `coursetype_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    cur.execute("SELECT * FROM `program_tbl`")
    data3 = cur.fetchall()
    #return list(data)
    print(list(data3))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data4 = cur.fetchall()
    #return list(data)
    print(list(data4))
    return render(request,'courseedit.html',{'mydata': data,'mydata1': data1,'mydata2': data2,'mydata3': data3,'mydata4': data4})

def course_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catcode = request.POST['code']
        catname = request.POST['name']
        catmaxmarks = request.POST['maxmarks']
        catminmarks = request.POST['minmarks']
        catcoursecategoryid = request.POST['cid']
        catcoursetypeid = request.POST['cid1']
        catpid = request.POST['pid']
        catfid = request.POST['fid']
        cur.execute("UPDATE `course_tbl` SET `course_code`= '{}',`course_name`= '{}',`course_maxmarks`= '{}',`course_minmarks`= '{}',`coursecategory_id`= '{}',`coursetype_id`= '{}',`program_id`= '{}',`faculty_id`='{}' WHERE  course_id = '{}'".format(catcode,catname,catmaxmarks,catminmarks,catcoursecategoryid,catcoursetypeid,catpid,catfid,catid))
        conn.commit()
        return redirect(course) 
    else:
        return redirect(course)

def coursedelete(request,id):
    print(id)
    cur.execute("delete from `course_tbl` where `course_id` = {}".format(id))
    conn.commit()
    return redirect(coursetable)



def assignment(request):
    cur.execute("SELECT * FROM `course_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'assignment.html',{'mydata': data})

def assignment_added(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['name']
        catsname = request.POST['sname']
        catremarks = request.POST['remarks']
        catsubmission = request.POST['submission']
        catid = request.POST['id']
        cur.execute("INSERT INTO `assignment_tbl`(`assignment_name`, `subject_name`, `remarks`, `assignment_submission`, `course_id`) VALUES ('{}','{}','{}','{}','{}')".format(catname,catsname,catremarks,catsubmission,catid))
        conn.commit()
        messages.info(request, 'Data Submitted Successfully')
        return redirect(assignment) 
    else:
        return redirect(assignment)
    
def assignmenttable(request):
    cur.execute('''SELECT
    `assignment_tbl`.`assignment_id`
    , `assignment_tbl`.`assignment_name`
    , `assignment_tbl`.`subject_name`
    , `assignment_tbl`.`remarks`
    , `assignment_tbl`.`assignment_submission`
    , `course_tbl`.`course_name`
FROM
    `course_tbl`
    INNER JOIN `assignment_tbl` 
        ON (`course_tbl`.`course_id` = `assignment_tbl`.`course_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'assignmenttable.html',{'mydata': data})   

def assignmentedit(request,id):
    cur.execute("SELECT * FROM `assignment_tbl` where assignment_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `course_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request,'assignmentedit.html',{'mydata': data,'mydata1': data1})

def assignment_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catname = request.POST['name']
        catsname = request.POST['sname']
        catremarks = request.POST['remarks']
        catsubmission = request.POST['submission']
        catcid = request.POST['cid']
        cur.execute("UPDATE `assignment_tbl` SET `assignment_name`= '{}',`subject_name`= '{}',`remarks`= '{}',`assignment_submission`= '{}',`course_id`='{}' WHERE   assignment_id = '{}'".format(catname,catsname,catremarks,catsubmission,catcid,catid))
        conn.commit()
        messages.info(request, 'Data Updated Successfully')
        return redirect(assignment) 
    else:
        return redirect(assignment)


def assignmentdelete(request,id):
    print(id)
    cur.execute("delete from `assignment_tbl` where `assignment_id` = {}".format(id))
    conn.commit()
    messages.info(request, 'Data Deleted Successfully')
    return redirect(assignmenttable)



def exam(request):
    cur.execute("SELECT * FROM `course_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'exam.html',{'mydata': data})

def exam_added(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['name']
        catschedule = request.POST['schedule']
        catid = request.POST['id']
        cur.execute("INSERT INTO `exam_tbl`( `exam_name`, `exam_timeschedule`, `course_id`)  VALUES ('{}','{}','{}')".format(catname,catschedule,catid))
        conn.commit()
        return redirect(exam) 
    else:
        return redirect(exam)

def examtable(request):
    cur.execute('''SELECT
    `exam_tbl`.`exam_id`
    , `exam_tbl`.`exam_name`
    , `exam_tbl`.`exam_timeschedule`
    , `course_tbl`.`course_name`
FROM
    `course_tbl`
    INNER JOIN `exam_tbl` 
        ON (`course_tbl`.`course_id` = `exam_tbl`.`course_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'examtable.html',{'mydata': data})

def examedit(request,id):
    cur.execute("SELECT * FROM `exam_tbl` where exam_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `course_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request,'examedit.html',{'mydata': data,'mydata1': data1})

def exam_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catname = request.POST['name']
        catschedule = request.POST['schedule']
        catcid = request.POST['cid']
        cur.execute("UPDATE `exam_tbl` SET `exam_name`= '{}',`exam_timeschedule`= '{}',`course_id`= '{}' WHERE   exam_id = '{}'".format(catname,catschedule,catcid,catid))
        conn.commit()
        return redirect(exam) 
    else:
        return redirect(exam)

def facultydelete(request,id):
    print(id)
    cur.execute("delete from `faculty_tbl` where `faculty_id` = {}".format(id))
    conn.commit()
    return redirect(facultytable)

def examdelete(request,id):
    print(id)
    cur.execute("delete from `exam_tbl` where `exam_id` = {}".format(id))
    conn.commit()
    return redirect(examtable)



def image(request):
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `notification_t_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'image.html',{'mydata': data,'mydata2': data2})

def image_added(request):
    if request.method == 'POST':
        print(request.POST)
        catfile = request.POST['file']
        catname = request.POST['name']
        catresolved = request.POST['resolved']
        catremarks = request.POST['remarks']
        catdate = request.POST['date']
        cattype = request.POST['type']
        catcid = request.POST['cid']
        catnid = request.POST['nid']
        cur.execute("INSERT INTO `image_tbl`(`image_file`, `image_name`, `resolved`, `remarks`, `image_date`, `image_querytype`, `crm_id`, `notification_id`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(catfile,catname,catresolved,catremarks,catdate,cattype,catcid,catnid))
        conn.commit()
        return redirect(image) 
    else:
        return redirect(image)

def imagetable(request):
    cur.execute("SELECT * FROM `image_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'imagetable.html',{'mydata': data})

def imageedit(request,id):
    cur.execute("SELECT * FROM `image_tbl` where image_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    cur.execute("SELECT * FROM `notification_t_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'imageedit.html',{'mydata': data,'mydata1': data1,'mydata2': data2})

def image_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catfile = request.POST['file']
        catname = request.POST['name']
        catresolved = request.POST['resolved']
        catremarks = request.POST['remarks']
        catdate = request.POST['date']
        cattype = request.POST['type']
        catcid = request.POST['cid']
        catnid = request.POST['nid']
        cur.execute("UPDATE `image_tbl` SET `image_file`= '{}',`image_name`= '{}',`resolved`= '{}',`remarks`= '{}',`image_date`= '{}',`image_querytype`= '{}',`crm_id`= '{}',`notification_id`= '{}' WHERE   image_id = '{}'".format(catfile,catname,catresolved,catremarks,catdate,cattype,catcid,catnid,catid))
        conn.commit()
        return redirect(image) 
    else:
        return redirect(image)

def imagedelete(request,id):
    print(id)
    cur.execute("delete from `image_tbl` where `image_id` = {}".format(id))
    conn.commit()
    return redirect(imagetable)



def sms(request):
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `notification_t_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'sms.html',{'mydata': data,'mydata2': data2})

def sms_added(request):
    if request.method == 'POST':
        print(request.POST)
        catdate = request.POST['date']
        catsentby = request.POST['sentby']
        catcid = request.POST['cid']
        catnid = request.POST['nid']
        cur.execute("INSERT INTO `sms_tbl`(`sms_date`, `sent_by`, `crm_id`, `notification_id`) VALUES ('{}','{}','{}','{}')".format(catdate,catsentby,catcid,catnid))
        conn.commit()
        return redirect(sms) 
    else:
        return redirect(sms)
    
def smstable(request):
    cur.execute("SELECT * FROM `sms_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'smstable.html',{'mydata': data})

def smsedit(request,id):
    cur.execute("SELECT * FROM `sms_tbl` where sms_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    cur.execute("SELECT * FROM `notification_t_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'smsedit.html',{'mydata': data,'mydata1': data1,'mydata2': data2})

def sms_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catdate = request.POST['date']
        catsenetby = request.POST['sentby']
        catcid = request.POST['cid']
        catnid = request.POST['nid']
        cur.execute("UPDATE `sms_tbl` SET `sms_date`= '{}',`sent_by`= '{}' ,`crm_id`= '{}',`notification_id`= '{}' WHERE   sms_id = '{}'".format(catdate,catsenetby,catcid,catnid,catid))
        conn.commit()
        return redirect(sms) 
    else:
        return redirect(sms)

def facultydelete(request,id):
    print(id)
    cur.execute("delete from `faculty_tbl` where `faculty_id` = {}".format(id))
    conn.commit()
    return redirect(facultytable)

def smsdelete(request,id):
    print(id)
    cur.execute("delete from `sms_tbl` where sms_id` = {}".format(id))
    conn.commit()
    return redirect(smstable)



def voice(request):
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `notification_t_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'voice.html',{'mydata': data,'mydata2': data2})

def voice_added(request):
    if request.method == 'POST':
        print(request.POST)
        catfile = request.POST['file']
        catdate = request.POST['date']
        catresolved = request.POST['resolved']
        catremarks = request.POST['remarks']
        catquerytype = request.POST['querytype']
        catcid = request.POST['cid']
        catnid = request.POST['nid']
        cur.execute("INSERT INTO `voice_tbl`( `voice_filename`, `voice_date` , `voice_resolved`, `remarks`, `voice_querytype`, `crm_id`, `notification_id`) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(catfile,catdate,catresolved,catremarks,catquerytype,catcid,catnid))
        conn.commit()
        return redirect(voice) 
    else:
        return redirect(voice)

def voicetable(request):
    cur.execute("SELECT * FROM `voice_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'voicetable.html',{'mydata': data})

def voiceedit(request,id):
    cur.execute("SELECT * FROM `faculty_tbl` where faculty_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    cur.execute("SELECT * FROM `notification_t_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'voiceedit.html',{'mydata': data,'mydata1': data1,'mydata2': data2})

def voice_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catfile = request.POST['file']
        catdate = request.POST['date']
        catresolved = request.POST['resolved']
        catremarks = request.POST['remarks']
        catquerytype = request.POST['querytype']
        catcid = request.POST['cid']
        catnid = request.POST['nid']
        cur.execute("UPDATE `voice_tbl` SET `voice_filename`= '{}',`voice_date`= '{}',`voice_resolved`= '{}',`remarks`= '{}',`voice_querytype`= '{}',`crm_id`= '{}',`notification_id`= '{}' WHERE  voice_id = '{}'".format(catfile,catdate,catresolved,catremarks,catquerytype,catcid,catnid,catid))
        conn.commit()
        return redirect(voice) 
    else:
        return redirect(voice)

def facultydelete(request,id):
    print(id)
    cur.execute("delete from `faculty_tbl` where `faculty_id` = {}".format(id))
    conn.commit()
    return redirect(facultytable)

def voicedelete(request,id):
    print(id)
    cur.execute("delete from `voice_tbl` where `voice_id` = {}".format(id))
    conn.commit()
    return redirect(voicetable)



def crmcomponent(request):
    cur.execute("SELECT * FROM `student_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'crmcomponent.html',{'mydata': data,'mydata2': data2})

def crmcomponent_added(request):
    if request.method == 'POST':
        print(request.POST)
        catcdate = request.POST['cdate']
        catcsubject = request.POST['csubject']
        catcdetails = request.POST['cdetails']
        catwsms=request.POST['wsms']
        catsms=request.POST['sms']
        catvoice=request.POST['voices']
        catimage=request.POST['image']
        catchatbot=request.POST['chatbot']
        catdinquiry=request.POST['dinquiry']
        catsid=request.POST['catsid']
        catfid=request.POST['catfid']
        cur.execute("INSERT INTO `crmcomponent_tbl`(`crm_date`, `crm_subject`, `crm_details`, `whatsapp_sms`,`sms`,`voice`,`image`,`chatbot`,`direct_inquiry`,`student_id`,`faculty_id`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(catcdate,catcsubject,catcdetails,catwsms,catsms,catvoice,catimage,catchatbot,catdinquiry,catsid,catfid))
        conn.commit()
        return redirect(crmcomponent) 
    else:
        return redirect(crmcomponent)

def crmcomponenttable(request):
    cur.execute('''SELECT
    `crmcomponent_tbl`.`crm_id`
    , `crmcomponent_tbl`.`crm_date`
    , `crmcomponent_tbl`.`crm_subject`
    , `crmcomponent_tbl`.`crm_details`
    , `crmcomponent_tbl`.`whatsapp_sms`
    , `crmcomponent_tbl`.`sms`
    , `crmcomponent_tbl`.`voice`
    , `crmcomponent_tbl`.`image`
    , `crmcomponent_tbl`.`chatbot`
    , `crmcomponent_tbl`.`direct_inquiry`
    , `user_tbl`.`first_name`
    , `user_tbl`.`middle_name`
    , `user_tbl`.`last_name`
    , `faculty_tbl`.`faculty_name`
FROM
    `student_tbl`
    INNER JOIN `crmcomponent_tbl` 
        ON (`student_tbl`.`student_id` = `crmcomponent_tbl`.`student_id`)
    INNER JOIN `faculty_tbl` 
        ON (`faculty_tbl`.`faculty_id` = `crmcomponent_tbl`.`faculty_id`)
    INNER JOIN `user_tbl` 
        ON (`user_tbl`.`userid` = `student_tbl`.`user_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'crmcomponenttable.html',{'mydata': data})

def crmcomponentedit(request,id):
    cur.execute("SELECT * FROM `crmcomponent_tbl` where crm_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `student_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'crmcomponentedit.html',{'mydata': data,'mydata1': data1,'mydata2': data2})

def crmcomponent_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catdate = request.POST['cdate']
        catsubject = request.POST['csubject']
        catdetails = request.POST['cdetails']
        catwsms = request.POST['wsms']
        catsms = request.POST['sms']
        catvoice = request.POST['voices']
        catimage = request.POST['image']
        catchatbot = request.POST['chatbot']
        catinquery = request.POST['dinquery']
        catsid = request.POST['sid']
        catfid = request.POST['fid']
        cur.execute("UPDATE `crmcomponent_tbl` SET `crm_date`= '{}',`crm_subject`= '{}',`crm_details`= '{}',`whatsapp_sms`= '{}',`sms`= '{}',`voice`= '{}',`image`= '{}',`chatbot`= '{}',`direct_inquiry`= '{}',`student_id`= '{}',`faculty_id`= '{}' WHERE   crm_id = '{}'".format(catdate,catsubject,catdetails,catwsms,catsms,catvoice,catimage,catchatbot,catinquery,catsid,catfid,catid))
        conn.commit()
        return redirect(crmcomponent) 
    else:
        return redirect(crmcomponent)

def facultydelete(request,id):
    print(id)
    cur.execute("delete from `faculty_tbl` where `faculty_id` = {}".format(id))
    conn.commit()
    return redirect(facultytable)

def crmcomponentdelete(request,id):
    print(id)
    cur.execute("delete from `crmcomponent_tbl` where `crm_id` = {}".format(id))
    conn.commit()
    return redirect(crmcomponenttable)



def whatsappsms(request):
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `notification_t_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'whatsappsms.html',{'mydata': data,'mydata2': data2})

def whatsappsms_added(request):
    if request.method == 'POST':
        print(request.POST)
        catdate = request.POST['date']
        catcontct = request.POST['contact']
        cattype = request.POST['type']
        catresolved = request.POST['resolved']
        catremarks = request.POST['remarks']
        catimgdate = request.POST['imgdate']
        catimgquerytype = request.POST['imgquerytype']
        catcid = request.POST['cid']
        catnid = request.POST['nid']
        cur.execute("INSERT INTO `whatsappsms_tbl`(`sms_date`, `sms_contact`, `type`, `resolved`,`remarks`,`image_date`,`image_querytype`,`crm_id`,`notification_id`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(catdate,catcontct,cattype,catresolved,catremarks,catimgdate,catimgquerytype,catcid,catnid))
        conn.commit()
        return redirect(whatsappsms) 
    else:
        return redirect(whatsappsms)

def whatsappsmsedit(request,id):
    cur.execute("SELECT * FROM `whatsappsms_tbl` where wsms_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    cur.execute("SELECT * FROM `notification_t_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'whatsappsmsedit.html',{'mydata': data,'mydata1': data1,'mydata2': data2})

def whatsappsms_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catdate = request.POST['date']
        catcontact = request.POST['contact']
        cattype = request.POST['type']
        catresolved = request.POST['resolved']
        catremarks = request.POST['remarks']
        catdate = request.POST['date']
        catquerytype = request.POST['querytype']
        catcid = request.POST['cid']
        catnid = request.POST['nid']
        cur.execute("UPDATE `whatsappsms_tbl` SET `sms_date`= '{}',`sms_contact`= '{}',`type`= '{}',`resolved`= '{}',`remarks`= '{}',`image_date`= '{}',`image_querytype`= '{}',`crm_id`= '{}',`notification_id`= '{}' WHERE  wsms_id = '{}'".format(catdate,catcontact,cattype,catresolved,catremarks,catquerytype,catcid,catnid,catid))
        conn.commit()
        return redirect(whatsappsms) 
    else:
        return redirect(whatsappsms)

def facultydelete(request,id):
    print(id)
    cur.execute("delete from `faculty_tbl` where `faculty_id` = {}".format(id))
    conn.commit()
    return redirect(facultytable)

def whatsappsmstable(request):
    cur.execute("SELECT * FROM `whatsappsms_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'whatsappsmstable.html',{'mydata': data})

def whatsappsmsdelete(request,id):
    print(id)
    cur.execute("delete from `whatsappsms_tbl` where `sms_id` = {}".format(id))
    conn.commit()
    return redirect(whatsappsmstable)



def chatbotquery(request):
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'chatbotquery.html',{'mydata': data})

def chatbotquery_added(request):
    if request.method == 'POST':
        print(request.POST)
        catchatbotquery = request.POST['chatbotquery']
        catchatbotquerytype = request.POST['chatbotquerytype']
        catcid = request.POST['cid']
        cur.execute("INSERT INTO `chatbot_query_tbl`(`chatbot_query`, `chatbot_querytype`, `crm_id`) VALUES ('{}','{}','{}')".format(catchatbotquery,catchatbotquerytype,catcid))
        conn.commit()
        return redirect(chatbotquery) 
    else:
        return redirect(chatbotquery)
    
def chatbotqueryedit(request,id):
    cur.execute("SELECT * FROM `chatbot_query_tbl` where chatbot_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request,'chatbotqueryedit.html',{'mydata': data,'mydata1': data1})

def chatbotquery_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catchatbotquery = request.POST['chatbotquery']
        catchatbotquerytype = request.POST['chatbotquerytype']
        catcid = request.POST['cid']
        cur.execute("UPDATE `chatbot_query_tbl` SET `chatbot_query`= '{}',`chatbot_querytype`= '{}',`crm_id`= '{}' WHERE  chatbot_id = '{}'".format(catchatbotquery,catchatbotquerytype,catcid,catid))
        conn.commit()
        return redirect(chatbotquery) 
    else:
        return redirect(chatbotquery)

def facultydelete(request,id):
    print(id)
    cur.execute("delete from `faculty_tbl` where `faculty_id` = {}".format(id))
    conn.commit()
    return redirect(facultytable)

def chatbotquerytable(request):
    cur.execute("SELECT * FROM `chatbot_query_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'chatbotquerytable.html',{'mydata': data})

def chatbotquerydelete(request,id):
    print(id)
    cur.execute("delete from `chatbot_query_tbl` where `chatbot_id` = {}".format(id))
    conn.commit()
    return redirect(chatbotquerytable)



def chatbotanswer(request):
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'chatbotanswer.html',{'mydata': data})

def chatbotanswer_added(request):
    if request.method == 'POST':
        print(request.POST)
        catchatbotanswer = request.POST['chatbotanswer']
        catisrelevant = request.POST['isrelevant']
        catcid = request.POST['cid']
        cur.execute("INSERT INTO `chatbot_answer_tbl`(`chatbot_answer`, `isrelevant`, `crm_id`) VALUES ('{}','{}','{}')".format(catchatbotanswer,catisrelevant,catcid))
        conn.commit()
        return redirect(chatbotanswer) 
    else:
        return redirect(chatbotanswer)

def chatbotanswertable(request):
    cur.execute("SELECT * FROM `chatbot_answer_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'chatbotanswertable.html',{'mydata': data})

def chatbotansweredit(request,id):
    cur.execute("SELECT * FROM `chatbot_answer_tbl` where chatbot_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `crmcomponent_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request,'chatbotansweredit.html',{'mydata': data,'mydata1': data1})

def chatbotanswer_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catchatbotanswer = request.POST['chatbotanswer']
        catisrelevant = request.POST['isrelevant']
        catcid = request.POST['cid']
        cur.execute("UPDATE `chatbot_answer_tbl` SET `chatbot_answer`= '{}',`isrevelant`= '{}',`crm_id`= '{}' WHERE  chatbot_id = '{}'".format(catchatbotanswer,catisrelevant,catcid,catid))
        conn.commit()
        return redirect(chatbotanswer) 
    else:
        return redirect(chatbotanswer)

def facultydelete(request,id):
    print(id)
    cur.execute("delete from `faculty_tbl` where `faculty_id` = {}".format(id))
    conn.commit()
    return redirect(facultytable)

def chatbotanswerdelete(request,id):
    print(id)
    cur.execute("delete from `chatbot_answer_tbl` where `chatbot_id` = {}".format(id))
    conn.commit()
    return redirect(chatbotanswertable)



def studentprogram_t(request):
    cur.execute("SELECT * FROM `student_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `program_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'studentprogram_t.html',{'mydata': data,'mydata2':data2})

def studentprogram_tadded(request):
    if request.method == 'POST':
        print(request.POST)
        catsid = request.POST['sid']
        catpid = request.POST['pid']
        cataddate = request.POST['addate']
        cur.execute("INSERT INTO `studentprogram_t_tbl`(`student_id`,`program_id`,`admissiondate`) VALUES ('{}','{}','{}')".format(catsid,catpid,cataddate))
        conn.commit()
        return redirect(studentprogram_t) 
    else:
        return redirect(studentprogram_t)

def studentprogram_ttable(request):
    cur.execute('''SELECT
    `user_tbl`.`first_name`
    , `user_tbl`.`middle_name`
    , `user_tbl`.`last_name`
    , `program_tbl`.`program_name`
    , `studentprogram_t_tbl`.`admissiondate`
FROM
    `student_tbl`
    INNER JOIN `studentprogram_t_tbl` 
        ON (`student_tbl`.`student_id` = `studentprogram_t_tbl`.`student_id`)
    INNER JOIN `user_tbl` 
        ON (`user_tbl`.`userid` = `student_tbl`.`user_id`)
    INNER JOIN `program_tbl` 
        ON (`program_tbl`.`program_id` = `studentprogram_t_tbl`.`program_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'studentprogram_ttable.html',{'mydata': data})

def studentprogram_tdelete(request,id):
    print(id)
    cur.execute("delete from `studentprogram_t_tbl` where `student_id` = {}".format(id))
    conn.commit()
    return redirect(studentprogram_ttable)



def studentassignment_t(request):
    cur.execute("SELECT * FROM `student_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `assignment_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'studentassignment_t.html',{'mydata': data,'mydata2': data2})

def studentassignment_tadded(request):
    if request.method == 'POST':
        print(request.POST)
        catstudid= request.POST['sid']
        catassid = request.POST['assid']
        catsubject = request.POST['catsubject']
        catmarks = request.POST['marks']
        cur.execute("INSERT INTO `studentassignment_t_tbl`(`student_id`,`assignment_id`,`subject_details`,`marks`) VALUES ('{}','{}','{}','{}')".format(catstudid,catassid,catsubject,catmarks))
        conn.commit()
        return redirect(studentassignment_t) 
    else:
        return redirect(studentassignment_t)

def studentassignment_ttable(request):
    cur.execute('''SELECT
    `user_tbl`.`first_name`
    , `user_tbl`.`middle_name`
    , `user_tbl`.`last_name`
    , `assignment_tbl`.`assignment_name`
    , `studentassignment_t_tbl`.`subject_details`
    , `studentassignment_t_tbl`.`marks`
FROM
    `assignment_tbl`
    INNER JOIN `studentassignment_t_tbl` 
        ON (`assignment_tbl`.`assignment_id` = `studentassignment_t_tbl`.`assignment_id`)
    INNER JOIN `student_tbl` 
        ON (`student_tbl`.`student_id` = `studentassignment_t_tbl`.`student_id`)
    INNER JOIN `user_tbl` 
        ON (`user_tbl`.`userid` = `student_tbl`.`user_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'studentassignment_ttable.html',{'mydata': data})

def studentassignment_tdelete(request,id):
    print(id)
    cur.execute("delete from `studentassignment_t_tbl` where `student_id` = {}".format(id))
    conn.commit()
    return redirect(studentassignment_ttable)



def notification_t(request):
    cur.execute("SELECT * FROM `user_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'notification_t.html',{'mydata': data,'mydata2': data2})

def notification_tadded(request):
    if request.method == 'POST':
        print(request.POST)
        catuserid = request.POST['userid']
        catfacid = request.POST['facid']
        cur.execute("INSERT INTO `notification_t_tbl`(`user_id`,`faculty_id`) VALUES ('{}','{}')".format(catuserid,catfacid))
        conn.commit()
        return redirect(notification_t) 
    else:
        return redirect(notification_t)

def notification_ttable(request):
    cur.execute('''SELECT
    `notification_t_tbl`.`notification_id`
    , `user_tbl`.`first_name`
    , `user_tbl`.`middle_name`
    , `user_tbl`.`last_name`
    , `faculty_tbl`.`faculty_name`
FROM
    `user_tbl`
    INNER JOIN `notification_t_tbl` 
        ON (`user_tbl`.`userid` = `notification_t_tbl`.`user_id`)
    INNER JOIN `faculty_tbl` 
        ON (`faculty_tbl`.`faculty_id` = `notification_t_tbl`.`faculty_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'notification_ttable.html',{'mydata': data})

def notification_tdelete(request,id):
    print(id)
    cur.execute("delete from `notification_t_tbl` where `notification_id` = {}".format(id))
    conn.commit()
    return redirect(notification_ttable)



def coursesemester_t(request):
    cur.execute("SELECT * FROM `course_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `semester_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'coursesemester_t.html',{'mydata': data,'mydata2': data2})

def coursesemester_tadded(request):
    if request.method == 'POST':
        print(request.POST)
        catcid = request.POST['cid']
        catsid = request.POST['sid']
        cur.execute("INSERT INTO `coursesemester_t_tbl`(`course_id`,`semester_id`) VALUES ('{}','{}')".format(catcid,catsid))
        conn.commit()
        return redirect(coursesemester_t) 
    else:
        return redirect(coursesemester_t)

def coursesemester_ttable(request):
    cur.execute('''SELECT
    `course_tbl`.`course_name`
    , `semester_tbl`.`semester_name`
FROM
    `course_tbl`
    INNER JOIN `coursesemester_t_tbl` 
        ON (`course_tbl`.`course_id` = `coursesemester_t_tbl`.`course_id`)
    INNER JOIN `semester_tbl` 
        ON (`semester_tbl`.`semester_id` = `coursesemester_t_tbl`.`semester_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'coursesemester_ttable.html',{'mydata': data})

def coursesemester_tdelete(request,id):
    print(id)
    cur.execute("delete from `coursesemester_t_tbl` where `course_id` = {}".format(id))
    conn.commit()
    return redirect(coursesemester_ttable)



def studentexam_t(request):
    cur.execute("SELECT * FROM `student_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `exam_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'studentexam_t.html',{'mydata': data,'mydata2': data2})

def studentexam_tadded(request):
    if request.method == 'POST':
        print(request.POST)
        catstudid=request.POST['sid']
        catexamid = request.POST['examid']
        catmarks = request.POST['marks']
        cur.execute("INSERT INTO `studentexam_t_tbl`(`student_id`,`exam_id`,`marks`) VALUES ('{}','{}','{}')".format(catstudid,catexamid,catmarks))
        conn.commit()
        return redirect(studentexam_t) 
    else:
        return redirect(studentexam_t)

def studentexam_ttable(request):
    cur.execute('''SELECT
    `user_tbl`.`first_name`
    , `user_tbl`.`middle_name`
    , `user_tbl`.`last_name`
    , `exam_tbl`.`exam_name`
    , `studentexam_t_tbl`.`marks`
FROM
    `student_tbl`
    INNER JOIN `studentexam_t_tbl` 
        ON (`student_tbl`.`student_id` = `studentexam_t_tbl`.`student_id`)
    INNER JOIN `user_tbl` 
        ON (`user_tbl`.`userid` = `student_tbl`.`user_id`)
    INNER JOIN `exam_tbl` 
        ON (`exam_tbl`.`exam_id` = `studentexam_t_tbl`.`exam_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'studentexam_ttable.html',{'mydata': data})

def studentexam_tdelete(request,id):
    print(id)
    cur.execute("delete from `studentexam_t_tbl` where `student_id` = {}".format(id))
    conn.commit()
    return redirect(studentexam_ttable)



def courseexam_t(request):
    cur.execute("SELECT * FROM `course_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `exam_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'courseexam_t.html',{'mydata': data,'mydata2': data2})

def courseexam_tadded(request):
    if request.method == 'POST':
        print(request.POST)
        catcourseid= request.POST['courseid']
        catexamid = request.POST['examid']
        cattmarks = request.POST['tmarks']
        cur.execute("INSERT INTO `courseexam_t_tbl`(`course_id`,`exam_id`,`total_marks`) VALUES ('{}','{}','{}')".format(catcourseid,catexamid,cattmarks))
        conn.commit()
        return redirect(courseexam_t) 
    else:
        return redirect(courseexam_t)

def courseexam_ttable(request):
    cur.execute('''SELECT
    `course_tbl`.`course_name`
    , `exam_tbl`.`exam_name`
    , `courseexam_t_tbl`.`total_marks`
FROM
    `course_tbl`
    INNER JOIN `courseexam_t_tbl` 
        ON (`course_tbl`.`course_id` = `courseexam_t_tbl`.`course_id`)
    INNER JOIN `exam_tbl` 
        ON (`exam_tbl`.`exam_id` = `courseexam_t_tbl`.`exam_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'courseexam_ttable.html',{'mydata': data})

def courseexam_tdelete(request,id):
    print(id)
    cur.execute("delete from `courseexam_t_tbl` where `course_id` = {}".format(id))
    conn.commit()
    return redirect(courseexam_ttable)



def sms_t(request):
    cur.execute("SELECT * FROM `sms_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'sms_t.html',{'mydata': data,'mydata2': data2})

def sms_tadded(request):
    if request.method == 'POST':
        print(request.POST)
        catsid = request.POST['sid']
        catfid = request.POST['fid']
        cur.execute("INSERT INTO `sms_t_tbl`(`sms_id`,`faculty_id`) VALUES ('{}','{}')".format(catsid,catfid))
        conn.commit()
        return redirect(sms_t) 
    else:
        return redirect(sms_t)

def sms_ttable(request):
    cur.execute('''SELECT
    `sms_tbl`.`sms_date`
    , `faculty_tbl`.`faculty_name`
FROM
    `sms_tbl`
    INNER JOIN `sms_t_tbl` 
        ON (`sms_tbl`.`sms_id` = `sms_t_tbl`.`sms_id`)
    INNER JOIN `faculty_tbl` 
        ON (`faculty_tbl`.`faculty_id` = `sms_t_tbl`.`faculty_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'sms_ttable.html',{'mydata': data})

def sms_tdelete(request,id):
    print(id)
    cur.execute("delete from `sms_t_tbl` where `sms_id` = {}".format(id))
    conn.commit()
    return redirect(sms_ttable)


# no change ...


def homepage(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html')

def data(request):
    return render(request,'data.html')

def general(request):
    return render(request,'general.html')

def index2(request):
    return render(request,'index2.html')

def logindesign(request):
    return render(request, 'login.html')

def loginview(request):
    if request.method == 'POST':
        print(request.POST)
        user_email = request.POST['txt1']
        user_password = request.POST['txt2']
        cur.execute("select * from `user_tbl` where `uemail` = '{}' and `password` = '{}'".format(user_email,user_password))
        data = cur.fetchone()
        if data is not None:
            if len(data) > 0:
                	#Fetch Data (ID and Email )
                user_id = data[0]
                user_name = data[1]
                user_email = data[6]
                user_type= data[25]
                print(user_id)
                print(user_email)
                	#Create Session Variable and Store UserID and UserEmail
                request.session['user_id'] = user_id
                request.session['user_name'] = user_name
                request.session['user_email'] = user_email
                request.session['user_type'] = user_type

                #Pass Message to Html Page
                #Create Cookie Variable and Store UserID and UserEmail redirect on Homepage
                response = redirect(homeview)
                response.set_cookie('user_id', user_id)
                response.set_cookie('user_name', user_name)
                response.set_cookie('user_email', user_email)
                response.set_cookie('user_type', user_type)

                return response
            else:
                messages.info(request, 'Details Not Found')
                return render(request, 'login.html') 
        messages.info(request, 'Login Failed')
        return render(request, 'login.html')
    else:
        return render(request, 'login.html') 


#HomePage with Authentication (Without Loing Home page will not open)
def homeview(request):
    if 'user_email' in request.COOKIES and request.session.has_key('user_email'):
        user_email = request.session['user_email']
        user_email = request.COOKIES['user_email']
        user_type = request.COOKIES['user_type']
        print("Session is  " + user_email)
        print("Cookie is  " + user_email)
        print("Cookie is  " + user_type)

        if user_type == 'student' or user_type == 'Student':
            return render(request, 'student/home.html')
        elif user_type == 'faculty' or user_type == 'Faculty':
            return render(request, 'faculty/home.html')
        else:
            return render(request, 'home.html')
    else:
        return redirect(loginview)



def forgotpassword(request):
    if request.method == 'POST':
        print(request.POST)
        user_email = request.POST['txt1']
        cur.execute("select * from `user_tbl` where `uemail` = '{}' ".format(user_email))
        db_data = cur.fetchone()
            
        if db_data is not None:
            if len(db_data) > 0:
                #Fetch Data
                user_id = db_data[0]
                user_db_password = db_data[24]
                print(user_id)
                print(user_db_password)
                #Mail Send Code
                subject = 'Forgot Password'
                message = ' Your Password is  ' + user_db_password
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user_email,]
                send_mail( subject, message, email_from, recipient_list )
                messages.success(request, 'Password Sent on your Email ID')
                return redirect(loginview)
            else:
                messages.success(request, 'Wrong Email Details')
                return render(request, 'forgotpassword.html') 
        messages.success(request, 'Wrong Email Details')
        return render(request, 'forgotpassword.html')
    else:
            return render(request, 'forgotpassword.html')



def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    del request.session['user_email']
    response =redirect(logindesign)
    response.delete_cookie('user_id')
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response

def changepassword(request):
    return  render(request,'changepassword.html')

def changepassword(request):
    if request.method == 'POST':
        if 'user_email' in request.COOKIES and request.session.has_key('user_email'):
            print(request.POST)
            user_email = request.session['user_email']
            print(user_email)
            opass = request.POST['opass']
            npass = request.POST['npass']
            cpass = request.POST['cpass']
            cur.execute("select * from `user_tbl` where `uemail` = '{}'".format(user_email))
            db_data = cur.fetchone()
            if db_data is not None:
                if len(db_data) > 0:
                    #Fetch Data
                    oldpassword = db_data[25]
                    if opass == oldpassword:
                        if npass == cpass:
                            cur.execute("update  `user_tbl` set `password` = {} where `uemail` = '{}'".format(npass,user_email))
                            conn.commit()
                            messages.success(request, 'Password Changed')
                            return render(request, 'changepassword.html')
                        else:
                            messages.success(request, 'New and Confirm Password not Match')
                            return render(request, 'login.html')
                    else:
                        messages.success(request, 'Old Password not match')
                        return render(request, 'changepassword.html')
                else:
                    messages.success(request, 'record not found ')
                    redirect(loginview) 
            else: 
                messages.success(request, 'Error ')
                redirect(loginview) 
        else:
            return redirect(loginview)
    else:
        return render(request, 'changepassword.html')