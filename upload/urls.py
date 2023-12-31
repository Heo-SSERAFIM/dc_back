
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path


urlpatterns = [

    path("admin/", admin.site.urls),
    path("upload/", include("uploadPage.urls")),
    path("feedback/", include("feedback.urls")),
    path("verify/", include("Verify.urls")),
    path("trend/", include("trend.urls")),
    path('search/', include("search.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?:.*)$', serve, {'document_root': settings.STATIC_ROOT, }),


]

