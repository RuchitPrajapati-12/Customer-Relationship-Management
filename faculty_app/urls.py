from django.urls import path
from . import views

urlpatterns =[

    path('',views.homepage,name='homepage'),

    path('crmcomponent',views.crmcomponent,name='crmcomponent'),
    path('crmcomponent_added',views.crmcomponent_added,name='crmcomponent_added'),
    path('crmcomponentdelete/<int:id>', views.crmcomponentdelete, name="crmcomponentdelete"),

    path('course',views.course,name='course'),
    path('course_added',views.course_added,name='course'),
    path('coursedelete/<int:id>', views.coursedelete, name="coursedelete"),

    path('semester',views.semester,name='semester'),
    path('semester_added',views.semester_added,name='semester'),
    path('semesterdelete/<int:id>', views.semesterdelete, name="semesterdelete"),

    path('sms_t',views.sms_t,name='sms_t'),
    path('sms_tadded',views.sms_tadded,name='sms_tadded'),
    path('sms_tdelete/<int:id>', views.sms_tdelete, name="sms_tdelete"),

    path('notification_t',views.notification_t,name='notification_t'),
    path('notification_tadded',views.notification_tadded,name='notification_tadded'),
    path('notification_tdelete/<int:id>', views.notification_tdelete, name="notification_tdelete"),

    path('crmcomponenttable',views.crmcomponenttable,name='crmcomponenttable'),
    path('crmcomponentedit/<int:id>',views.crmcomponentedit,name='crmcomponentedit'),
    path('/faculty/crmcomponent_update',views.crmcomponent_update,name='crmcomponent_update'), 

    path('assignment',views.assignment,name='assignmenttable'),
        path('assignment_added',views.assignment_added,name='assignmenttable'),


    path('assignmenttable',views.assignmenttable,name='assignmenttable'),
    path('assignmentedit/<int:id>',views.assignmentedit,name='assignmentedit'),
    path('/faculty/assignment_update',views.assignment_update,name='assignment_update'), 
       
    path('coursetable',views.coursetable,name='coursetable'),
    path('courseedit/<int:id>',views.courseedit,name='courseedit'),
    path('/faculty/course_update',views.course_update,name='course_update'),
       
    path('semestertable',views.semestertable,name='semestertable'),
    path('semesteredit/<int:id>',views.semesteredit,name='semesteredit'),
    path('/faculty/semester_update',views.semester_update,name='semester_update'),
       
    path('sms_ttable',views.sms_ttable,name='sms_ttable'),
    path('notification_ttable',views.notification_ttable,name='notification_ttable'),

]