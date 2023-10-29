from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reviews, Playlist


# Create your forms here.

# https://ordinarycoders.com/blog/article/django-user-register-login-logout
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)  # required to create a user account

    class Meta:
        model = User
        fields = (
            "username", "email", "password1",
            "password2")  # fields that appear on register form (password2 is validation)

    def save(self, commit=True):  # saves the email to user
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']  # render info to form

        if commit:
            user.save()

        return user


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('title', 'review', 'rating', 'song')


class CreatePlayForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('title', 'song')
