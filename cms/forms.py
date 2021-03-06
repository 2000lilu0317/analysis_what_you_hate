#これは情報を共有するためのやつ
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import UserPostModel
UserModel = get_user_model()


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['username'].widget.attrs['class'] = 'input'
       self.fields['password'].widget.attrs['class'] = 'input'

class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'twitter')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'

class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('no_one', 'no_two')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'

class UserPostForm(forms.ModelForm) :
   class Meta :
       model = UserPostModel
       fields=("no_one","no_two")

   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field in self.fields.values():
           field.widget.attrs['class'] = 'input'