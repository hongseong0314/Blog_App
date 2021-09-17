from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlog, BlogCommentForm
from .models import Blog, Comment
# Create your views here.
def index(request):
	return render(request, 'index.html')

def blogmain(request):
	blogs = Blog.objects.all()
	return render(request, 'blogmain.html', {'blogs':blogs})

def createblog(request):
	if request.method == "POST":
		form = CreateBlog(request.POST)

		if form.is_valid():
			form.save()
			return redirect("blogmain")
		else:
			return redirect("index")
	else:
		form = CreateBlog()
		return render(request, "createblog.html", {'form':form})

def detail(request, blog_id):
	blog_detail = get_object_or_404(Blog, pk=blog_id)
	comments = Comment.objects.filter(blog_id=blog_id)

	if request.method == "POST":
		comment_form = BlogCommentForm(request.POST)

		if comment_form.is_valid():
			content = comment_form.cleaned_data['comment_textfiels']
			print(content)


			login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'
 
			client_id = 'a4d343564aae96dcf88be4dd3f9209ba'
			redirect_uri = 'http://127.0.0.1:8000/oauth'
			 
			login_request_uri += 'client_id=' + client_id
			login_request_uri += '&redirect_uri=' + redirect_uri
			login_request_uri += '&response_type=code'
			
			return redirect(login_request_uri)
		else:
			return redirect('blogmain')
	else:
		comment_form = BlogCommentForm()
		context = {
			"blog_detail" : blog_detail,
			"comments" : comments,
			"comment_form" : comment_form
		}


	return render(request, "detail.html", context)

def oauth(request):
	code = request.GET['code']
	print('code = ' + str(code))
	return redirect('blogmain')