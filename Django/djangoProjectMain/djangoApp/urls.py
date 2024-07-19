from django.urls import path
from . import views
# . means current directory
urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.index1, name = 'index1'),
    path('update/<str:usn>/', views.updateStudent, name='update_student'),
    path('delete/<str:usn>/', views.deleteStudent, name='delete_student'),
    path('update-delete', views.update_delete, name='update_delete')
]
