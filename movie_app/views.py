from enum import auto
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from .models import Movie

from .serializers import MovieSerializer
from .serializers import UserSerializer

# Create your views here.
class UserRegister(APIView):
    permission_classes = (AllowAny, )
    def post(self, request):
        password = request.data['password']
        user_serializer = UserSerializer(data={**request.data})
        if user_serializer.is_valid():
            user = User.objects.create(**request.data)
            user.set_password(password)
            user.save()
            final_res = UserSerializer(user)
            return Response(data={'user': final_res.data})
        return Response({'msg': 'Create user is failed', 'error': user_serializer.errors})


class GetAllUsers(APIView):
    permssion_classes = [AllowAny, ]
    authentication_classes = []
    def get(self, request):
        users = User.objects.all()
        print('USERS-----', users)
        user_serializer = UserSerializer(users, many=True)
        return Response({'user data': user_serializer.data})


class ListAllMoviesAPI(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        movie_serializer = MovieSerializer(movies, many=True)
        return Response(movie_serializer.data)


class GetMovieDetailsAPI(APIView):
    def get(self, request):
        movie = Movie.objects.get(pk=id)


def movie_details(request, movie_id):
	try:
		movie_info = Movie.objects.get(pk=movie_id)
		shows = Show.objects.filter(movie=movie_id,
			date=datetime.date.today()).order_by('theatre')
		show_list = []
		show_by_theatre = []
		theatre = shows[0].theatre
		for i in range(0, len(shows)):
			if theatre != shows[i].theatre:
				theatre = shows[i].theatre
				show_list.append(show_by_theatre)
				show_by_theatre = []
			show_by_theatre.append(shows[i])

		show_list.append(show_by_theatre)

	except Movie.DoesNotExist:
		raise Http404("Page does not exist")
	return render(request, 'movie/movie_details.html',
		{'movie_info': movie_info, 'show_list': show_list})


# class GetSeatDetailsAPI(APIView):
    



# class UpdateBlogAPI(APIView):
#     permission_classes = (IsAuthenticated, )
#     def put(self, request, id=None):
#         print('user ****',request.user)
#         blog = Blog.objects.get(id=id)
#         author = blog.author
#         print('Author *****', author)
#         if request.user == blog.author:
#             blog_Serializer = BlogSerializer(blog, data=request.data)
#             if blog_Serializer.is_valid():
#                 blog_Serializer.save()
#                 return Response(blog_Serializer.data)
#             return Response(blog_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({'msg': 'Unauthorized request'})

#     def delete(self, request, id):
#         blog = Blog.objects.get(id=id)
#         print('USER *****', request.user)
#         print('AUTHOR ****', blog.author)
#         if request.user == blog.author:
#             blog.delete()
#             msg = f'Blog with ID {id} deleted successfully'
#             return Response({'msg': msg})
#         return Response({'msg': 'Unauthorized request'})

    
# class CreateBlogAPI(APIView):
#     permission_classes = (IsAuthenticated, )
#     def post(self, request):
#         blog = request.data
#         print('UID ****', request.user.id)
#         blog_serializer = BlogSerializer(data=blog)
#         if blog_serializer.is_valid():
#             blog_serializer.save()
#             return Response({'msg': 'Created Blog successfully'})
#         return Response({'msg': 'Invalid data', 'err': blog_serializer.errors})