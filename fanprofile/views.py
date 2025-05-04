from django.shortcuts import render, redirect
import tweepy
from django.contrib.auth import login, logout
from .models import FanProfile, Tweets, Medalha
from .forms import FanProfileForm, CustomUserCreationForm, CustomAuthenticationForm

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAADKV0wEAAAAA9yY9%2Fyck0nH%2BTcu7FtfkYd2x8DY%3DbjxWvB4eKQHqDVJjlk9uFMyPbYUgw8dQIzwDEJOd0pKgfeI42i')

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('perfil')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'cadastro.html', {'form':form})

def LoginPage(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('perfil')

    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def perfil(request):
    if not request.user.is_authenticated:
        return redirect('cadastro')

    form = None
    tweet = None

    try:
        perfil = FanProfile.objects.get(user=request.user)
        tweet = Tweets.objects.filter(fanprofile=perfil).order_by('-id')[:5]
        try:
            conquistarMedalha(perfil)
        except Exception as e:
            print("Erro em conquistarMedalha:", e)
            traceback.print_exc()
        perfil.save()
    except Exception as e:
        print("Erro ao carregar perfil:", e)
        traceback.print_exc()
        perfil = None
        if request.method == 'POST':
            form = FanProfileForm(request.POST)
            if form.is_valid():
                novo_perfil = form.save(commit=False)
                novo_perfil.user = request.user
                novo_perfil.save()

                try:
                    tweets = tweetsFuria(novo_perfil.twitter)
                    for t in tweets:
                        Tweets.objects.create(fanprofile=novo_perfil, texto=t['texto'])
                    novo_perfil.interacoes += len(tweets)
                    novo_perfil.save()
                except Exception as e:
                    print("Erro ao buscar tweets:", e)
                    traceback.print_exc()

                return redirect('perfil')
        else:
            form = FanProfileForm()

    return render(request, 'perfil.html', {'form': form, 'perfil': perfil, 'tweet': tweet})

def tweetsFuria(username):
    user = client.get_user(username=username)
    user_id = user.data.id
    tweets = client.get_users_tweets(id=user_id)

    tweets_furia = []
    if tweets.data:
        for tweet in tweets.data:
            if 'furia' in tweet.text.lower() or '@furiagg' in tweet.text.lower():
                tweets_furia.append({
                    'texto': tweet.text,
                })

    return tweets_furia

def logoutPage(request):
    logout(request)
    return redirect('home')

def conquistarMedalha(perfil):
    interacoes = perfil.interacoes

    if interacoes >= 5:
        medalha= Medalha.objects.get(nome="Medalha Iniciante")
        perfil.medalhas.add(medalha)

    if interacoes >= 10:
        medalha = Medalha.objects.get(nome="Medalha Torcedor")
        perfil.medalhas.add(medalha)

    if interacoes >= 30:
        medalha= Medalha.objects.get(nome="Medalha FURIOSO")
        perfil.medalhas.add(medalha)

def atualizarTweets(request):
    perfil = FanProfile.objects.get(user=request.user)
    novos_tweets = tweetsFuria(perfil.twitter)

    for tweet in novos_tweets:
        Tweets.objects.create(fanprofile=perfil, texto=tweet['texto'])

    perfil.interacoes += len(novos_tweets)
    perfil.save()

    return redirect('perfil')


