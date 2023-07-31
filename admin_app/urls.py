from django.urls import path
from . import views

urlpatterns =[
       
       #  form render | data insert in xampp 

       path('country', views.country, name="country"),
       path('country_added', views.country_added, name="country"),
       path('countrydelete/<int:id>', views.countrydelete, name="countrydelete"),
       
       path('state',views.state,name='state'),
       path('state_added',views.state_added,name='state'),
       path('statedelete/<int:id>', views.statedelete, name="statedelete"),
       
       path('city',views.city,name='city'),
       path('city_added',views.city_added,name='city'),
       path('citydelete/<int:id>', views.citydelete,name='citydelete'),
       
       path('program',views.program,name='program'),
       path('program_added',views.program_added,name='program'),
       path('programdelete/<int:id>', views.programdelete, name="programdelete"),
       
       path('semester',views.semester,name='semester'),
       path('semester_added',views.semester_added,name='semester'),
       path('semesterdelete/<int:id>', views.semesterdelete, name="semesterdelete"),
       
       path('user',views.user,name='user'),
       path('user_added',views.user_added,name='user'),
       path('userdelete/<int:id>', views.userdelete, name="userdelete"),
       
       path('studentform',views.studentform,name='studentform'),
       path('student_added',views.student_added,name='studentadded'),
       path('studentdelete/<int:id>', views.studentdelete, name="studentdelete"),
       
       path('facultyform',views.facultyform,name='facultyform'),
       path('faculty_added',views.faculty_added,name='facultyadded'),
       path('facultydelete/<int:id>', views.facultydelete, name="facultydelete"),
       
       path('coursecategory',views.coursecategory,name='coursecategory'),
       path('coursecategory_added',views.coursecategory_added,name='coursecategory'),
       path('coursecategorydelete/<int:id>', views.coursecategorydelete, name="coursecategorydelete"),
       
       path('coursetype',views.coursetype,name='coursetype'),
       path('coursetype_added',views.coursetype_added,name='coursetype'),
       path('coursetypedelete/<int:id>', views.coursetypedelete, name="coursetypedelete"),
       
       path('course',views.course,name='course'),
       path('course_added',views.course_added,name='course'),
       path('coursedelete/<int:id>', views.coursedelete, name="coursedelete"),
       
       path('assignment',views.assignment,name='assignment'),
       path('assignment_added',views.assignment_added,name='assignment'),
       path('assignmentdelete/<int:id>', views.assignmentdelete, name="assignmentdelete"),
       
       path('exam',views.exam,name='exam'),
       path('exam_added',views.exam_added,name='exam'),
       path('examdelete/<int:id>', views.examdelete, name="examdelete"),
       
       path('image',views.image,name='image'),
       path('image_added',views.image_added,name='image'),
       path('imagedelete/<int:id>', views.imagedelete, name="imagedelete"),
       
       path('sms',views.sms,name='sms'),
       path('sms_added',views.sms_added,name='sms'),
       path('smsdelete/<int:id>', views.smsdelete, name="smsdelete"),
       
       path('voice',views.voice,name='voice'),
       path('voice_added',views.voice_added,name='voice'),
       path('voicedelete/<int:id>', views.voicedelete, name="voicedelete"),

       path('crmcomponent',views.crmcomponent,name='crmcomponent'),
       path('crmcomponent_added',views.crmcomponent_added,name='crmcomponent_added'),
       path('crmcomponentdelete/<int:id>', views.crmcomponentdelete, name="crmcomponentdelete"),

       path('whatsappsms',views.whatsappsms,name='whatsappsms'),
       path('whatsappsms_added',views.whatsappsms_added,name='whatsappsms_added'),
       path('whatsappsmsdelete/<int:id>', views.whatsappsmsdelete, name="whtsappsmsdelete"),

       path('chatbotquery',views.chatbotquery,name='chatbotquery'),
       path('chatbotquery_added',views.chatbotquery_added,name='chatbotquery_added'),
       path('chatbotquerydelete/<int:id>', views.chatbotquerydelete, name="chatbotquerydelete"),

       path('chatbotanswer',views.chatbotanswer,name='chatbotanswer'),
       path('chatbotanswer_added',views.chatbotanswer_added,name='chatbotanswer_added'),
       path('chatbotanswerdelete/<int:id>', views.chatbotanswerdelete, name='chatbotanswerdelete'),

       path('studentprogram_t',views.studentprogram_t,name='studentprogram_t'),
       path('studentprogram_tadded',views.studentprogram_tadded,name='studentprogram_tadded'),
       path('studentprogram_tdelete/<int:id>', views.studentprogram_tdelete, name="studentprogram_tdelete"),

       path('studentassignment_t',views.studentassignment_t,name='studentassignment_t'),
       path('studentassignment_tadded',views.studentassignment_tadded,name='studentassignment_tadded'),
       path('studentassignment_tdelete/<int:id>', views.studentassignment_tdelete, name="studentassignment_tdelete"),

       path('notification_t',views.notification_t,name='notification_t'),
       path('notification_tadded',views.notification_tadded,name='notification_tadded'),
       path('notification_tdelete/<int:id>', views.notification_tdelete, name="notification_tdelete"),

       path('coursesemester_t',views.coursesemester_t,name='coursesemester_t'),
       path('coursesemester_tadded',views.coursesemester_tadded,name='coursesemester_tadded'),
       path('coursesemester_tdelete/<int:id>', views.coursesemester_tdelete, name="coursesemester_tdelete"),

       path('studentexam_t',views.studentexam_t,name='studentexam_t'),
       path('studentexam_tadded',views.studentexam_tadded,name='studentexam_tadded'),
       path('studentexam_tdelete/<int:id>', views.studentexam_tdelete, name="studentexam_tdelete"),

       path('courseexam_t',views.courseexam_t,name='courseexam_t'),
       path('courseexam_tadded',views.courseexam_tadded,name='courseexam_tadded'),
       path('courseexam_tdelete/<int:id>', views.courseexam_tdelete, name="courseexam_tdelete"),

       path('sms_t',views.sms_t,name='sms_t'),
       path('sms_tadded',views.sms_tadded,name='sms_tadded'),
       path('sms_tdelete/<int:id>', views.sms_tdelete, name="sms_tdelete"),
       
       
       # no change ....
       
       path('',views.logindesign,name='login'),
       path('loginview',views.loginview,name='loginview'),
       
       path('forgotpassword',views.forgotpassword,name='login'),

       path('logout',views.logout,name='logout'),
       path('changepassword',views.changepassword,name='changepassword'),
       path('home',views.homeview,name='home'),
       path('base',views.base,name='base'),
       path('data',views.data,name='data'),
       path('general',views.general,name='general'),
       path('index2',views.index2,name='index2'),
       
       
       
       # all table .....
  
       
       path('countrytable',views.countrytable,name='countrytable'),
       path('countryedit/<int:id>',views.countryedit,name='countryedit'),
       path('country_update',views.country_update,name='country_update'),

       path('statetable',views.statetable,name='statetable'),
       path('stateedit/<int:id>',views.stateedit,name='stateedit'),
       path('state_update',views.state_update,name='state_update'),

       path('citytable',views.citytable,name='citytable'),
       path('cityedit/<int:id>',views.cityedit,name='cityedit'),
       path('city_update',views.city_update,name='city_update'),
       
       path('usertable',views.usertable,name='usertable'),
       path('useredit/<int:id>',views.useredit,name='useredit'),
       path('user_update',views.user_update,name='user_update'),

       path('programtable',views.programtable,name='programtable'),
       path('programedit/<int:id>',views.programedit,name='programedit'),
       path('program_update',views.program_update,name='program_update'),
       
       path('semestertable',views.semestertable,name='semestertable'),
       path('semesteredit/<int:id>',views.semesteredit,name='semesteredit'),
       path('semester_update',views.semester_update,name='semester_update'),
       
       path('studenttable',views.studenttable,name='studenttable'),
       path('studentformedit/<int:id>',views.studentformedit,name='studentformedit'),
       path('student_update',views.student_update,name='student_update'),
       
       path('facultytable',views.facultytable,name='facultytable'),
       path('facultyformedit/<int:id>',views.facultyformedit,name='facultyformedit'),
       path('faculty_update',views.faculty_update,name='faculty_update'),
       
       
       path('coursecategorytable',views.coursecategorytable,name='coursecategorytable'),
       path('coursecategoryedit/<int:id>',views.coursecategoryedit,name='coursecategoryedit'),
       path('coursecategory_update',views.coursecategory_update,name='coursecategory_update'),
       
       path('coursetypetable',views.coursetypetable,name='coursetypetable'),
       path('coursetypeedit/<int:id>',views.coursetypeedit,name='coursetypeedit'),
       path('coursetype_update',views.coursetype_update,name='coursetype_update'),
       
       path('coursetable',views.coursetable,name='coursetable'),
       path('courseedit/<int:id>',views.courseedit,name='courseedit'),
       path('course_update',views.course_update,name='course_update'),
       
       path('assignmenttable',views.assignmenttable,name='assignmenttable'),
       path('assignmentedit/<int:id>',views.assignmentedit,name='assignmentedit'),
       path('assignment_update',views.assignment_update,name='assignment_update'),
       
       
       path('imagetable',views.imagetable,name='imagetable'),
       path('imageedit/<int:id>',views.imageedit,name='imageedit'),
       path('image_update',views.image_update,name='image_update'),
       
       path('examtable',views.examtable,name='examtable'),
       path('examedit/<int:id>',views.examedit,name='examedit'),
       path('exam_update',views.exam_update,name='exam_update'),
       
       path('smstable',views.smstable,name='smstable'),
       path('smsedit/<int:id>',views.smsedit,name='smsedit'),
       path('sms_update',views.sms_update,name='sms_update'),
       
       path('voicetable',views.voicetable,name='voicetable'),  
       path('voiceedit/<int:id>',views.voiceedit,name='voiceedit'),
       path('voice_update',views.voice_update,name='voice_update'),
       
       path('crmcomponenttable',views.crmcomponenttable,name='crmcomponenttable'),
       path('crmcomponentedit/<int:id>',views.crmcomponentedit,name='crmcomponentedit'),
       path('crmcomponent_update',views.crmcomponent_update,name='crmcomponent_update'), 
       
       path('whatsappsmstable',views.whatsappsmstable,name='whatsappsmstable'),
       path('whatsappsmsedit/<int:id>',views.whatsappsmsedit,name='whatsappsmsedit'),
       path('whatsappsms_update',views.whatsappsms_update,name='whatsappsms_update'), 
       
       path('chatbotquerytable',views.chatbotquerytable,name='chatbotquerytable'),
       path('chatbotqueryedit/<int:id>',views.chatbotqueryedit,name='chatbotqueryedit'),
       path('chatbotquery_update',views.chatbotquery_update,name='chatbotquery_update'),
       
       path('chatbotanswertable',views.chatbotanswertable,name='chatbotanswertable'),
       path('chatbotansweredit/<int:id>',views.chatbotansweredit,name='chatbotansweredit'),
       path('chatbotanswer_update',views.chatbotanswer_update,name='chatbotanswer_update'), 
       
       
       path('studentprogram_ttable',views.studentprogram_ttable,name='studentprogram_ttable'),
       path('studentassignment_ttable',views.studentassignment_ttable,name='studentassignment_ttable'),
       path('notification_ttable',views.notification_ttable,name='notification_ttable'),
       path('coursesemester_ttable',views.coursesemester_ttable,name='coursesemester_ttable'),
       path('studentexam_ttable',views.studentexam_ttable,name='studentexam_ttable'),
       path('courseexam_ttable',views.courseexam_ttable,name='courseexam_ttable'),
       path('sms_ttable',views.sms_ttable,name='sms_ttable')

]