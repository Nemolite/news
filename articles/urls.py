from django.urls import path, include

from . import admin
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'post', NewsViewSet)

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

    path('formtest/',formtest,name='formtest' ),

    # Каталог
    path('shop/',shop,name='shop' ),

    # path('api/v1/postlist/', NewsAPIView.as_view()),
    # path('api/v1/postlist/<int:pk>/', NewsAPIView.as_view())
    # path('api/v1/postlist/', NewsAPIList.as_view()),
    # path('api/v1/postlist/<int:pk>/', NewsAPIList.as_view()),
    # path('api/v1/postlist/<int:pk>/', NewsAPIUpdate.as_view()),
    # path('api/v1/postlist/<int:pk>/', NewsAPIDelete.as_view()),
    # path('api/v1/postdetail/<int:pk>/', NewsAPIDetailView.as_view())

    # path('api/v1/postlist/', NewsViewSet.as_view({'get':'list'})),
    # path('api/v1/postlist/<int:pk>/', NewsViewSet.as_view({'put':'update'})),
    path('api/v1/', include(router.urls)),
]