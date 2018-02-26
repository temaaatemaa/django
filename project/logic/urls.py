from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainView, name='main'),
    url(r'^setup_user/(?P<pk>.+)/$',views.setupUser,name='setupUser'),
    url(r'^add_row/(?P<fio>.+)/(?P<system>.+)/(?P<priority>.+)/(?P<time>.+)/$',views.addRow,name='addRow'),
    url(r'^del_row/(?P<fio>.+)/(?P<system>.+)/(?P<priority>.+)/(?P<time>.+)/$',views.delRow,name='delRow'),
    url(r'^add_situation/(?P<system>.+)/(?P<priority>.+)/(?P<time>.+)/$',views.addSituation,name='addSituation'),
    url(r'^setup_user/$',views.setupUserNull,name='setupUserNull'),
    url(r'^download/(?P<path>.*)$',views.download,name='download')
]