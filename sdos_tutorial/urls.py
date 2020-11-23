from django.urls import path, include
from user.views import PersonViewSet
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path

router = DefaultRouter()
router.register('person', PersonViewSet, basename='person')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),

]
