from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ExtendedUser


class ExtendedUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = ExtendedUser
        fields = UserCreationForm.Meta.fields + ('email',)


class ExtendedUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = ExtendedUser
        fields = UserChangeForm.Meta.fields
