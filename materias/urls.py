from django.urls import path

from . import views

app_name = 'materias'
urlpatterns = [
    path('', views.list_materias, name='main'),
    path('<int:materia_id>/', views.detail_materia, name='detail'), 
    path('search/', views.search_materias, name='search'),
    path('create/', views.create_materias, name='create'), 
    path('update/<int:materia_id>/', views.update_materia, name='update'),
    path('delete/<int:materia_id>/', views.delete_materia, name='delete'),
]