from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('eliminar/<str:modelo>/<int:item_id>/', views.eliminar_item, name='eliminar_item'),
    path('editar/<str:modelo>/<int:item_id>/', views.editar_item, name='editar_item'),

]
