from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.signout, name='signout'),
    path('todopage/', views.todo, name='todopage'),
    path('edit_todo/<int:srno>/', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>/', views.delete_todo, name='delete_todo'),

]