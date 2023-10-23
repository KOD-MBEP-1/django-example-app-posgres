from django.contrib import admin
from django.urls import include, path
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]
