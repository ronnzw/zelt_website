from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('our_products/', views.our_products, name='our_products'),
	path('contact/', views.contact, name='contact'),
	path('thanks/', views.thanks, name='thanks'),
	]