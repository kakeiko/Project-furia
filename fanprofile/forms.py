from django import forms
from .models import FanProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={
        'class': 'input-nick',
        'placeholder': 'Username'
    }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'input-pass',
        'placeholder': 'Digite a senha'
    }))

    class Meta:
        model = User
        fields = ['username', 'password',]

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={
        'class': 'input-nick',
        'placeholder': 'Username'
    }))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'input-pass',
        'placeholder': 'Digite a senha'
    }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'input-pass-confirm',
        'placeholder': 'Confirme a senha'
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class FanProfileForm(forms.ModelForm):
    class Meta:
        model = FanProfile
        fields = ['jogos_favoritos', 'jogador_favorito', 'tipo_conteudo', 'twitter']
        labels = {
            'jogos_favoritos': '',
            'jogador_favorito': '',
            'tipo_conteudo': '',
            'twitter': '',
        }
        widgets = {
            'jogos_favoritos': forms.TextInput(attrs={'class': 'input-jogos',
        'placeholder': 'Jogos favoritos'}),
            'jogador_favorito': forms.TextInput(attrs={'class': 'input-jogador',
        'placeholder': 'Jogador favorito'}),
            'tipo_conteudo': forms.TextInput(attrs={'class': 'input-tipo',
        'placeholder': 'tipo de conteúdo'}),
            'twitter': forms.TextInput(attrs={'class': 'input-twitter',
        'placeholder': 'Twitter(sem o @)'}),
        }