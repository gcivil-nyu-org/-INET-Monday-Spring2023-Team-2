from profiles.views.activate_email import activate
from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

from profiles.views.home import home
from profiles.views.profile import ProfileView
from profiles.views.profile import profile_update


urlpatterns = [
    path("", home, name="home"),
    re_path(r"^profile/$", ProfileView.as_view(), name="profile"),
    re_path(r"^profile/update/$", profile_update, name="profile_update"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
