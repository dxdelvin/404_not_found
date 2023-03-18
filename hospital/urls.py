
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('saveform', views.saveform, name="saveform"),
    path('dashboard/<str:username>', views.dashboard, name="dashboard"),
    path('admin_only/', views.admin_only_view, name='admin_only'),
]
