from django.urls import path
from movies.views import *
app_name = 'movies'

urlpatterns = [
    path('create/', MovieCreateView.as_view(), name='create_movie'),
    path('list/', MovieListView.as_view(), name='movie_list'),
    path('delete/<int:pk>', MovieDeleteView.as_view(), name='movie_delete'),
    path('update/<int:pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('detail/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]