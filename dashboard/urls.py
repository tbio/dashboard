# Django Modules
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Third Party Modules
from rest_framework import routers

# App Modules
from api.views import MeasurementViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('^measurements', MeasurementViewSet)
router.register('^users', UserViewSet)


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls)),
    url(r'^', include('accounts.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
