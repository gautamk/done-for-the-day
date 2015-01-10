from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin

admin.autodiscover()
admin.site.login = login_required(admin.site.login)
urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'googlelogin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'googlelogin.views.login', name='login'),
    url(r'^oauth2/redirect/$', 'googlelogin.views.oauth2redirect', name='oauth2redirect')
)
