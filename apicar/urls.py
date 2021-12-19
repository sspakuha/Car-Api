from django.conf.urls import url 
from apicar import views
from django.urls import path, include
 
urlpatterns = [ 
    path('cars', views.cars, name="cars"),
	 path('cars/<int:id>', views.delete, name="delete"),
	 path('rate', views.rate, name="rate"),
	 path('popular', views.popular, name="popular")
]