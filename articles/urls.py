from django.urls import path, include

from . import admin
from .views import *

urlpatterns = [
    path('',index,name='index' ),
    path('category/<int:id>/',category,name='category' ),
    path('post/<int:id>/',post,name='post' ),

    path('dbtrening/',dbtrening,name='dbtrening' ),
    path('insert/',insert,name='insert' ),
    path('gett/',gett,name='gett' ),
    path('updater/',updater,name='updater' ),
    path('myforms/',myforms,name='myforms' ),
    path('myforms/insforms/',insforms,name='insforms' ),
    path('spec/',spec,name='spec' ),

    path('tomany/',manytomany,name='tomany' ),
    path('stud/<int:id>/',stud,name='stud' ),
    path('curs/<int:id>/',curs,name='curs' ),

    path('test/',test,name='test' ),


]