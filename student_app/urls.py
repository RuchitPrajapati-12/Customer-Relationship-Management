from django.urls import path
from . import views

urlpatterns =[

    path('studentprogram_t',views.studentprogram_t,name='studentprogram_t'),
    path('studentprogram_tadded',views.studentprogram_tadded,name='studentprogram_tadded'),
    path('studentprogram_tdelete/<int:id>', views.studentprogram_tdelete, name="studentprogram_tdelete"),
    path('studentprogram_tedit/<int:id>', views.studentprogram_tedit, name="studentprogram_tedit"),
    path('studentprogram_tupdate/<int:id>', views.studentprogram_tupdate, name="studentprogram_tupdate"),

    path('studentassignment_t',views.studentassignment_t,name='studentassignment_t'),
    path('studentassignment_tadded',views.studentassignment_tadded,name='studentassignment_tadded'),
    path('studentassignment_tdelete/<int:id>', views.studentassignment_tdelete, name="studentassignment_tdelete"),
    #path('studentassignment_tedit/<int:id>', views.studentassignment_tedit, name="studentassignment_tedit"),
    #path('studentassignment_tupdate/<int:id>', views.studentassignment_tupdate, name="studentassignment_tupdate"),

    path('crmcomponent',views.crmcomponent,name='crmcomponent'),
    path('crmcomponent_added',views.crmcomponent_added,name='crmcomponent_added'),
    path('crmcomponentdelete/<int:id>', views.crmcomponentdelete, name="crmcomponentdelete"),

    path('program',views.program,name='program'),
    path('program_added',views.program_added,name='program'),
    path('programdelete/<int:id>', views.programdelete, name="programdelete"),

    path('studentexam_t',views.studentexam_t,name='studentexam_t'),
    path('studentexam_tadded',views.studentexam_tadded,name='studentexam_tadded'),
    path('studentexam_tdelete/<int:id>', views.studentexam_tdelete, name="studentexam_tdelete"),


    path('',views.homepage,name='homepagestudent'),
    path('programtable',views.programtable,name='programtable'),
    path('programedit/<int:id>',views.programedit,name='programedit'),
    path('/student/program_update',views.program_update,name='program_update'),
    
    path('crmcomponenttable',views.crmcomponenttable,name='crmcomponenttable'),
    path('crmcomponentedit/<int:id>',views.crmcomponentedit,name='crmcomponentedit'),
    path('/student/crmcomponent_update',views.crmcomponent_update,name='crmcomponent_update'), 
       
    path('studentprogram_ttable',views.studentprogram_ttable,name='studentprogram_ttable'),
    path('studentassignment_ttable',views.studentassignment_ttable,name='studentassignment_ttable'),
    path('studentexam_ttable',views.studentexam_ttable,name='studentexam_ttable'),

]