from django.contrib import admin
from django.urls import path
from qtb_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.view_items, name='dashboard')
]
