from django.urls import path 
from .views import MovieDetail, MovieList

urlpatterns = [
    path('api/movies',MovieList.as_view(),name='movies_list'),
    path('api/movies/<int:pk>/',MovieDetail.as_view(),name='movies_detail'),

]
