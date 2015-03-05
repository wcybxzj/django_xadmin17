from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
import xadmin

from xadmin.plugins import xversion
xversion.register_models()

from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^', include(xadmin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
=======
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^blog/', include('blog.urls')),
    url(r'^', include(xadmin.site.urls))
>>>>>>> 876e8a2b99035bf5d5faae56fda480bf4112a089
)
