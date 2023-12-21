from django import forms
from allauth.account.forms import SignupForm
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'type' , 'category']




class MyCustomSignupForm(SignupForm):

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        return user
        common = Group.objects.get(name='common')
        common.user_set.add(user)