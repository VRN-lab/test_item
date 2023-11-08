from django.urls import path
from django.views.generic import RedirectView

from menu import views


app_name = 'menu'

urlpatterns = [
    path('', RedirectView.as_view(url='index/')),
    path('<path:page>/', views.menu_pages, name='menu_pages'),
]
