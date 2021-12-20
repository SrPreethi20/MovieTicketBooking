from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from .views import (
    ListAllMoviesAPI,
    GetMovieDetailsAPI,
    UserRegister, 
    GetAllUsers,
    # CreateBlogAPI
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('all-movies/', ListAllMoviesAPI.as_view(), name='all_movies'),
    path('movie/<int:id>/', GetMovieDetailsAPI.as_view(), name='all_movies'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)