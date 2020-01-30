from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import LoginApi

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = LoginApi
        fields = ('email', 'username')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = LoginApi
        fields = ('email', 'password', 'username', 'is_active', 'is_admin', 'is_staff','is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]




class AccountAdmin(UserAdmin):
     # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display= ["email","username","date_joined","last_login","is_admin","is_staff","is_superuser"]
    list_filter = ('is_admin',)

    search_fields = ["email"]
    readonly_fields = ["date_joined","last_login"]
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    ordering = ('email',)






admin.site.site_header = 'CustomEverything'
admin.site.register(LoginApi,AccountAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)