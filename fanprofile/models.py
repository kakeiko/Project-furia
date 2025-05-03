from django.db import models
from django.contrib.auth.models import User

class Medalha(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=255)
    criterio = models.CharField(max_length=255)
    
class FanProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jogos_favoritos = models.CharField(max_length=255)
    jogador_favorito = models.CharField(max_length=100)
    tipo_conteudo = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    interacoes = models.IntegerField(default=0)
    foto = models.ImageField(upload_to="fotos", blank=True, null=True)
    medalhas = models.ManyToManyField(Medalha, blank=True)

    def __str__(self):
        return f'perfil de {self.user.username}'

class Tweets(models.Model):
    fanprofile = models.ForeignKey(FanProfile, on_delete=models.CASCADE, related_name='tweets')
    texto = models.TextField()

