from django.conf.urls import url
from . import views

urlpatterns = [
    # urls jorge, tambien modificado urls.py en /tbd
    url(r'^sites/(?P<site_pk>\d+)/new_image/$', views.new_image_site, name='new_image_site'),
    url(r'^sites/(?P<site_pk>\d+)/new_object$', views.new_object, name='new_object'),
    url(r'^sites/objects/edit/(?P<object_pk>\d+)$', views.edit_object, name='edit_object'),
    url(r'^sites/objects/delete/(?P<object_pk>\d+)$', views.delete_object, name='delete_object'),
    url(r'^sites/objects/(?P<object_pk>\d+)/new_image/$', views.new_image_object, name='new_image_object'),
    url(r'^sites/list/$', views.list_sites, name='list_sites'),
    url(r'^sites/(?P<site_pk>\d+)/list_objects/$', views.list_objects, name='list_objects'),
    url(r'^sites/gallery/$', views.gallery_sites, name='gallery_sites'),
    url(r'^sites/gallery/page=(?P<page>\d+)$', views.gallery_sites, name='gallery_sites_page'),
    url(r'^sites/photos/delete/(?P<photo_pk>\d+)$', views.delete_photo_site, name='delete_photo_site'),
    url(r'^sites/objects/photos/delete/(?P<photo_pk>\d+)$', views.delete_photo_object, name='delete_photo_object'),
    url(r'^gallery/objects/$', views.gallery_objects, name='gallery_objects'),
    url(r'^object/(?P<object_pk>\d+)/$', views.object_page, name='object_page'),
]
