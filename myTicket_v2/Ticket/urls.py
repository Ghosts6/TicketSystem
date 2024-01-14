from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('main/', views.main, name='main'),
    path('status/', views.status, name='status'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('locked/', views.locked, name='locked'),
    path('home/login/',views.user_login, name='login'),
    path('main/status',views.status, name='status'),
]

