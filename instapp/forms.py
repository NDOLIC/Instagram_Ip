from django import forms
from . models import IGPost, UserProfile, Comment, Like
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostPictureForm(forms.ModelForm):
    class Meta:
        model = IGPost
        fields = ['title', 'image']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


