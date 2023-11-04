from django.urls import path

from . import views

app_name = 'materias'
urlpatterns = [
    path('', views.list_materias, name='main'),
    path('confirm_delete/', views.confirm_delete, name='confirm_delete'),
    path('<int:materia_id>/', views.detail_materia, name='detail'), 
    path('search/', views.search_materias, name='search'),
    path('create/', views.create_materias, name='create'), 
    path('delete/<int:materia_id>/', views.delete_materia, name='delete'),
    path('update/<int:materia_id>/', views.update_materia, name='update'),
]