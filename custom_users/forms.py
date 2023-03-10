from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        form = CustomUser
        fields = UserCreationForm.Meta.fields + ("bio",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        form = CustomUser
        fields = UserCreationForm.Meta.fields + ("bio",)
