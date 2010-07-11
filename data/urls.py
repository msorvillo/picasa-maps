from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('picasa-maps.data.views',
    (r'^latlong/$', 'latlong'),
    (r'^latlong/(?P<date>\d+)/$', 'latlong'),
    (r'^albums/(?P<location_id>\d+)/$', 'albums'),
    #(r'^photos/(?P<album_name>\d+)/$', 'albums'),
)
