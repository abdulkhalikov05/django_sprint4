from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Comment, Post


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Адрес электронной почты',
        help_text='Обязательное поле. Введите действительный email.'
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует.')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M', 
                attrs={'type': 'datetime-local'}
            )
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')