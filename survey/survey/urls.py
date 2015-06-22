from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls.views import *
from main.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
                       
    #main
    url(r'^$',               'main.views.index',                                                  name='index'),
    url(r'write/$',          'main.views.write',                                                  name='write'),
    url(r'^login/$',         'django.contrib.auth.views.login', {'template_name' : 'login.html'}, name='login'),
    url(r'^signup/$',        'main.views.signup',                                                 name='signup'),
    url(r'^signup/submit/$', 'main.views.signup_submit',                                          name='signup_submit'),
    url(r'^logout/$',        'main.views.user_logout',                                            name='user_logout'),
    url(r'^write/$',         'main.views.write',                                                  name='write'),
    url(r'^submit_write/$',  'main.views.submit_write',                                           name='submit_write'),
    
    #polls
    url(r'^polls/$',                                          'polls.views.index'    , name='index2'),   
    url(r'^polls/(?P<poll_id>\d+)/$',                         'polls.views.detail'   , name='detail'),   
    url(r'^polls/(?P<poll_id>\d+)/vote/(?P<choice_id>\d+)/$', 'polls.views.vote'     , name='vote'),   
    url(r'^polls/(?P<poll_id>\d+)/result/$',                  'polls.views.result'   , name='result'),
    url(r"^polls/add/$",                                      add_poll, name="add_poll"),
    url(r"^polls/submit/$",                                   submit_poll           , name='submit_poll'),

)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

