from django.urls import path
from . import views

urlpatterns = [
    path('brews/', views.brews, name='brews'),
    path('brews/add/', views.add_brew, name='add_brew'),
    path('brews/update/<int:brew_id>/', views.update_brew, name='update_brew'),
    path('brews/delete/<int:brew_id>/', views.delete_brew, name='delete_brew'),
    path('beans/', views.beans, name='beans'),
    path('beans/add/', views.add_bean, name='add_bean'),
    path('beans/update/<int:bean_id>/', views.update_bean, name='update_bean'),
    path('beans/delete/<int:bean_id>/', views.delete_bean, name='delete_bean')
]