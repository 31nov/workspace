from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
                       
    #main
    url(r'main/$',                                           'main.views.index'     , name='index'),                   
    
    #polls
    url(r'polls/$',                                          'polls.views.index'    , name='index'),   
    url(r'polls/(?P<poll_id>\d+)/$',                         'polls.views.detail'   , name='detail'),   
    url(r'polls/(?P<poll_id>\d+)/vote/(?P<choice_id>\d+)/$', 'polls.views.vote'     , name='vote'),   
    url(r'polls/(?P<poll_id>\d+)/result/$',                  'polls.views.result'   , name='result'),
    
    
)
