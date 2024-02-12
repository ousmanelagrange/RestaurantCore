
from django.contrib import admin
from django.urls import path, include
from Menu.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'core_api'), namespace='core_api')),
]
