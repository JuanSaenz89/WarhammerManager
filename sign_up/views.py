from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
# Create your views here.

def sign_up(request):
    sign_form = SignUpForm()
    log_in_form = LoginForm()
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:

            return render(request, 'sign_up/sign_up.html', {'error': 'Passwords do not match', 'form': sign_form})
        # You can add more fields like email if needed
        if username and password:

            try:

                user = User.objects.create_user(username=username,email=email , password=password, is_staff=True, is_superuser=True )
                user.save()
                return render(request, 'sign_up/login.html', {'message': 'User created successfully. Please log in.', 'form': log_in_form})
            
            except Exception as e:

                if 'UNIQUE constraint' in str(e):

                    return render(request, 'sign_up/sign_up.html', {'error': 'Username already exists','form': sign_form})
                return render(request, 'sign_up/sign_up.html', {'error': 'Error creating user','form': sign_form})
        else:
            return render(request, 'sign_up/sign_up.html', {'error': 'Please provide both username and password','form': sign_form})
    return render(request, 'sign_up/sign_up.html', {'form': sign_form})


def login(request):
    login_form = LoginForm()
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'core/home.html', {'message': 'Logged in successfully'})
        else:
            return render(request, 'sign_up/login.html', {'error': 'Invalid username or password', 'form': login_form})
    
    return render(request, 'sign_up/login.html', {'form': login_form})
    

def log_out(request):
    auth_logout(request)
    return render(request, 'core/home.html', {'message': 'Logged out successfully'})