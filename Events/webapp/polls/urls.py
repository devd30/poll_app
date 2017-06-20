
from django.conf.urls import url

from . import views

app_name ='polls'

urlpatterns = [
    url(r'^loginid/$', views.loginid, name='login'),
    #url(r'^authen/$',views.authenticate , name = 'authen'),
    # ex: /polls/
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^logoutid/$' , views.logoutid , name = 'logoutid'),

    url(r'^addquestion/$' , views.addquestion , name = 'addquestion'),

    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    #url(r'^(?P<question_id>[0-9]+)/logoutid/$', views.logoutid, name='logoutid'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    #url(r'^(?P<question_id>[0-9]+)/results/logoutid/$', views.logoutid, name='logoutid'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^(?P<question_id>[0-9]+)/fetchvote/$', views.fetchvote, name='fetchvote'),

    url(r'^fetchdata/$', views.fetchdata, name='fetch'), 

    url(r'^fetchit/$', views.fetchit, name='fetchit'),

    url(r'^comment/$', views.comment, name='comment'), 

    url(r'^image/$', views.image, name='image'), 

    url(r'^getimage/$', views.getImage, name='getimage'),

    url(r'^fetchQuestion/$', views.fetchQuestion, name='fetchques'),

    url(r'^questionurl/$', views.questionurl, name='quest'),

    url(r'^questionurls/$', views.questionurls, name='quests'),

    url(r'^questionaddreact/$', views.questionaddreact, name='questreact'),

    url(r'^questionadd/$', views.questionadd, name='questadd'),

]
