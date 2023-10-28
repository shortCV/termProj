from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)  # required to create a user account

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")  # fields that appear on register form (password2 is validation)

    def save(self, commit=True):  # saves the email to user
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']  # render info to form

        if commit:
            user.save()

        return user
