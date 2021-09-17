from django import forms
from .models import Blog, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class CreateBlog(forms.ModelForm):
	class Meta:
		model = Blog

		fields = ["title", "author", "body"]

		weights = {
			"title":forms.TextInput(attrs={"class":"form-control", "style":"width: 100%", "placeholder":"제목을 입력하시오."}),
			"author":forms.Select(attrs={"class":"custom-select"}),
			"body":forms.CharField(widget=CKEditorUploadingWidget)
		}

class BlogCommentForm(forms.ModelForm):
	class Meta:
		model = Comment

		fields = ["comment_textfiels"]
		widgets = {
			'comment_textfiels' : forms.Textarea(attrs={'class':'form-control', 'rows': 4, 'cols': 40}) 
		}