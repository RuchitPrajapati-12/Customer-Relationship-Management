from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

import mysql.connector as mcdb

conn = mcdb.connect(host="localhost", user="root", passwd="", database='crm2')
print('Successfully connected to database')

def homepage(request):
    return render(request,'faculty/home.html')

cur = conn.cursor()

def crmcomponent(request):
    cur.execute("SELECT * FROM `student_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'faculty/crmcomponent.html',{'mydata': data,'mydata2': data2})

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
    return render(request,'faculty/crmcomponenttable.html',{'mydata': data})

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
    return render(request,'faculty/crmcomponentedit.html',{'mydata': data,'mydata1': data1,'mydata2': data2})

def crmcomponent_update(request):
    if request.method == 'POST':
        print(request.POST)
        cid = request.POST['txt1']
        catdate = request.POST['date']
        catsub = request.POST['subject']
        catdet = request.POST['details']
        catwsms = request.POST['wsms']
        catsms = request.POST['sms']
        catvoice = request.POST['voices']
        catimg = request.POST['image']
        catchatbot = request.POST['chatbot']
        catdinq = request.POST['dinq']
        catsid = request.POST['sid']
        catfid = request.POST['fid']
        cur.execute("UPDATE `crmcomponent_tbl` SET `crm_date`='{}',`crm_subject`='{}',`crm_details`='{}',`whatsapp_sms`='{}',`sms`='{}',`voice`='{}',`image`='{}',`chatbot`='{}',`direct_inquiry`='{}',`student_id`='{}',`faculty_id`='{}'  where  `crm_id` = '{}' ".format(catdate,catsub,catdet,catwsms,catsms,catvoice,catimg,catchatbot,catdinq,catsid,catfid,cid))
        conn.commit()
        return redirect(crmcomponent) 
    else:
        return redirect(crmcomponent)

def crmcomponentdelete(request,id):
    print(id)
    cur.execute("delete from `crmcomponent_tbl` where `crm_id` = {}".format(id))
    conn.commit()
    return redirect(crmcomponenttable)



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
    return render(request,'faculty/course.html',{'mydata': data,'mydata2':data2,'mydata3':data3,'mydata4':data4})

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
    return render(request,'faculty/coursetable.html',{'mydata': data})

def courseedit(request,id):
    cur.execute("SELECT * FROM `course_tbl` where course_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request,'faculty/courseedit.html',{'mydata': data})

def course_update(request):
    if request.method == 'POST':
        print(request.POST)
        cid = request.POST['txt1']
        catcode = request.POST['code']
        catname = request.POST['name']
        catmax = request.POST['maxmarks']
        catmin = request.POST['minmarks']
        catcatid = request.POST['cid']
        cattypeid = request.POST['cid1']
        catpid = request.POST['pid']
        catfid = request.POST['fid']
        cur.execute("UPDATE `course_tbl` SET `course_code`='{}',`course_name`='{}',`course_maxmarks`='{}',`course_minmarks`='{}',`coursecategory_id`='{}',`coursetype_id`='{}',`program_id`='{}',`faculty_id`='{}'   where  `course_id` = '{}' ".format(catcode,catname,catmax,catmin,catcatid,cattypeid,catpid,catfid,cid))
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
    return render(request,'faculty/assignment.html',{'mydata': data})

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
        
        #mail code for all student
        cur.execute("SELECT * FROM `user_tbl` where usertype  = 'Student' ")
        data = cur.fetchall()

        for i in data:
            myemail = i[6]
            subject = 'New Assignment Added ' 
            message =  "Assignment Name" +catname + " date " + catsubmission
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [myemail,]
            send_mail( subject, message, email_from, recipient_list )
            print("Mailllllllll")
        messages.info(request, 'Data Submitted Successfully')
        return redirect(assignmenttable) 
    else:
        return redirect(assignmenttable)
    
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
    return render(request,'faculty/assignmenttable.html',{'mydata': data})   

def assignmentedit(request,id):
    cur.execute("SELECT * FROM `assignment_tbl` where assignment_id = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `course_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request,'faculty/assignmentedit.html',{'mydata': data,'mydata1': data1})

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



def semester(request):
    cur.execute("SELECT * FROM `program_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'faculty/semester.html',{'mydata': data,'mydata2': data2})

def semester_added(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['name']
        catpid = request.POST['programid']
        catfid = request.POST['facultyid']
        cur.execute("INSERT INTO  semester_tbl (semester_name, program_id, faculty_id) VALUES ('{}','{}','{}')".format(catname,catpid,catfid))
        conn.commit()
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
    return render(request,'faculty/semestertable.html',{'mydata': data})

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
        return redirect(semester) 
    else:
        return redirect(semester)

def semesterdelete(request,id):
    print(id)
    cur.execute("delete from `semester_tbl` where `semester_id` = {}".format(id))
    conn.commit()
    return redirect(semestertable)



def sms_t(request):
    cur.execute("SELECT * FROM `sms_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'faculty/sms_t.html',{'mydata': data,'mydata2': data2})

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
    return render(request,'faculty/sms_ttable.html',{'mydata': data})

def sms_tdelete(request,id):
    print(id)
    cur.execute("delete from `sms_t_tbl` where `sms_id` = {}".format(id))
    conn.commit()
    return redirect(sms_ttable)



def notification_t(request):
    cur.execute("SELECT * FROM `user_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `faculty_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'faculty/notification_t.html',{'mydata': data,'mydata2': data2})

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
    return render(request,'faculty/notification_ttable.html',{'mydata': data})

def notification_tdelete(request,id):
    print(id)
    cur.execute("delete from `notification_t_tbl` where `notification_id` = {}".format(id))
    conn.commit()
    return redirect(notification_ttable)