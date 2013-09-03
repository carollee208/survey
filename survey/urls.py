from django.conf.urls import patterns, include, url
from questions.views import questions, thanks
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('questions.views',
    url(r'^questions/$', questions), 
    url(r'^thanks/$', thanks),
    # Examples:
    # url(r'^$', 'survey.views.home', name='home'),
    # url(r'^survey/', include('survey.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
