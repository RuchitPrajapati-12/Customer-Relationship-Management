from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import mysql.connector as mcdb

conn = mcdb.connect(host="localhost", user="root", passwd="", database='crm2')
print('Successfully connected to database')

def homepage(request):
    return render(request,'student/home.html')

cur = conn.cursor()

def studentprogram_t(request):
    cur.execute("SELECT * FROM `student_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `program_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'student/studentprogram_t.html',{'mydata': data,'mydata2':data2})

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
    return render(request,'student/studentprogram_ttable.html',{'mydata': data})

def studentprogram_tedit(request,id):
    cur.execute("SELECT * FROM `studentprogram_t_tbl` where student_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request,'student/studentprogram_tedit.html',{'mydata': data})

def studentprogram_tupdate(request):
    if request.method == 'POST':
        print(request.POST)
        sid = request.POST['sid']
        pid = request.POST['pid']
        catdate = request.POST['adddate']
        cur.execute("UPDATE `studentprogram_t_tbl` SET `program_id`='{}',`admissiondate`='{}' WHERE `student_id`='{}'".format(sid,pid,catdate))
        conn.commit()
        return redirect(studentprogram_t) 
    else:
        return redirect(studentprogram_t)

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
    return render(request,'student/studentassignment_t.html',{'mydata': data,'mydata2': data2})

def studentassignment_tadded(request):
    if request.method == 'POST':
        print(request.POST)
        catstudid= request.COOKIES['user_id']
        catassid = request.POST['assid']
        catsubject = request.POST['catsubject']
        myfile = request.FILES['file123']
        fs = FileSystemStorage()
        resume = fs.save(myfile.name, myfile)
        cur.execute("INSERT INTO `studentassignment_t_tbl`(`student_id`,`assignment_id`,`subject_details`,`filepath`) VALUES ('{}','{}','{}','{}')".format(catstudid,catassid,catsubject,myfile))
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
    , `studentassignment_t_tbl`.`filepath`
    
FROM
    `assignment_tbl`
    INNER JOIN `studentassignment_t_tbl` 
        ON (`assignment_tbl`.`assignment_id` = `studentassignment_t_tbl`.`assignment_id`)
    
    INNER JOIN `user_tbl` 
        ON (`user_tbl`.`userid` = `studentassignment_t_tbl`.`student_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'student/studentassignment_ttable.html',{'mydata': data})

def studentassignment_tdelete(request,id):
    print(id)
    cur.execute("delete from `studentassignment_t_tbl` where `student_id` = {}".format(id))
    conn.commit()
    return redirect(studentassignment_ttable)



def crmcomponent(request):
    cur.execute("SELECT * FROM `student_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'student/crmcomponent.html',{'mydata': data,'mydata2': data2})

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
    return render(request,'student/crmcomponenttable.html',{'mydata': data})

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

def crmcomponentdelete(request,id):
    print(id)
    cur.execute("delete from `crmcomponent_tbl` where `crm_id` = {}".format(id))
    conn.commit()
    return redirect(crmcomponenttable)



def program(request):
    cur.execute("SELECT * FROM `student_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'student/program.html',{'mydata': data})

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
    return render(request,'student/programtable.html',{'mydata': data})

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
        return redirect(program) 
    else:
        return redirect(program)

def programdelete(request,id):
    print(id)
    cur.execute("delete from `program_tbl` where `program_id` = {}".format(id))
    conn.commit()
    return redirect(programtable)



def studentexam_t(request):
    cur.execute("SELECT * FROM `student_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `exam_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'student/studentexam_t.html',{'mydata': data,'mydata2': data2})

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
    return render(request,'student/studentexam_ttable.html',{'mydata': data})

def studentexam_tdelete(request,id):
    print(id)
    cur.execute("delete from `studentexam_t_tbl` where `student_id` = {}".format(id))
    conn.commit()
    return redirect(studentexam_ttable)