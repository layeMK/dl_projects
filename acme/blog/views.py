from django.shortcuts import render

from .mocks import Post

def index(request):
	posts = Post.all()
	return render(request, 'blog/index.html', {'posts_list': posts})


def show(request, id):
	post = Post.find(id)
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