from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^signup_success/$', views.signup_success, name='signup_success'),
    url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
    url(r'^profile/(?P<username>[-_\w.]+)/followers/$', views.followers, name='followers'),
    url(r'^profile/(?P<username>[-_\w.]+)/following/$', views.following, name='following'),
    url(r'^post/$', views.post_picture, name='post_picture'),
    url(r'^post/(?P<pk>\d+)/likes/$', views.likes, name='likes'),
    url(r'^like/$', views.add_like, name='like'),
    url(r'^comment/$', views.add_comment, name='comment')
]
if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
