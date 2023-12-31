from django.contrib import admin
from django.urls import path
from qtb_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.view_items, name='dashboard'),
    path('teams/', views.team_list, name='teams-view'),
    path('get_report_details/', views.get_report_details, name='get_report_details'),
]
