from django import forms
from . models import IGPost, UserProfile, Comment, Like


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


class PostPictureForm(ModelForm):
    class Meta:
        model = IGPost
        fields = ['title', 'image']


class ProfileEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'description']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


