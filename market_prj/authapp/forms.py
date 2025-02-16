from dataclasses import fields

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import HiddenInput, ModelForm

from authapp.models import BuyerUser, BuyerUserProfile


class BuyerUserRegisterForm(UserCreationForm):
    class Meta:
        model = BuyerUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class BuyerUserEditForm(UserChangeForm):
    class Meta:
        model = BuyerUser
        fields = ('username', 'first_name', 'email', 'phone_number', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = HiddenInput()


class BuyerUserLoginForm(AuthenticationForm):
    class Meta:
        model = BuyerUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class BuyerUserProfileEditForm(ModelForm):
    class Meta:
        model = BuyerUserProfile
        fields = ('location',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'