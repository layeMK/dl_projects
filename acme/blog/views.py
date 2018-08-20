from django.shortcuts import render, get_object_or_404
from django.http import Http404
#from .mocks import Post
from .models import Post

def index(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', {'posts_list': posts})


def show(request, id):
	try:
		post = Post.objects.get(pk=id)
	except Post.DoesNotExist:
		raise Http404('Sorry, Post #{} not found !'.format(id))

	#ou sinon on peut faire tout simple ci-dessous
	#
	#post=get_object_or_404(Post, pk=id)
	#
	#il faut au préalable avoir importé get_object_or_404 depuis django.shortcuts

	return render(request, 'blog/show.html', {'post': post})








# posts = [
# 		{'id':'1', 'title':'First Post', 'body':'This is my first post'},
# 		{'id':'2', 'title':'Second Post', 'body':'This is my second post'},
# 		{'id':'3', 'title':'Third Post', 'body':'This is my third post'},
# 	]

# def index(request):
	
# 	return render(request, 'blog/index.html', {'posts_list': posts})


# def show(request, id):
	
# 	return render(request, 'blog/show.html', {'post': posts[int(id) - 1]})