from django import forms
from django.contrib.auth.models import User
from .models import List

class UserFrom(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', )


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('title', )
