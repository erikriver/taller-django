from django.conf.urls.defaults import patterns, include, url
from plus.views import StatusCreate, PlusOne
from django.contrib.auth.decorators import login_required

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djplus_v1.views.home', name='home'),
    # url(r'^djplus_v1/', include('djplus_v1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^index/', login_required(StatusCreate.as_view())),
    url(r'^vote/', login_required(PlusOne.as_view())),
#    url(r'^my_status/', 'plus.views.my_status')
)
