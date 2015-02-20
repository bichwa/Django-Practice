from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Meta: 
		model = Post # Class Meta tells django which model should be used to create the form
		fields = ('title', 'text',)