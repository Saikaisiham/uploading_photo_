import logging
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


logging.basicConfig(level=logging.DEBUG)


users_register_handler = logging.FileHandler('logs/users_register.log')
users_login_handler = logging.FileHandler('logs/users_login.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
users_register_handler.setFormatter(formatter)
users_login_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(users_register_handler)
logger.addHandler(users_login_handler)

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                logger.info(f"The account for user '{user.username}' has been successfully created")
                cleaned_data = form.cleaned_data
                logger.debug(f"Cleaned data: {cleaned_data}")
                return redirect('/')
            except Exception as e:
                logger.error(f"Error saving user: {e}", exc_info=True)
        else:
            logger.debug(f"Form data: {request.POST}")
            logger.debug(f"Is form valid? {form.is_valid()}")

    else:
        form = NewUserForm()

    return render(request, 'auth_user/register.html', context={"form": form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info(f'You are now logged in as {username}.')
                return redirect('/user/login')
            else:
                logger.error('Invalid username or password')
        else:
            logger.error('Invalid username or password')
    form = AuthenticationForm()
    return render(request,'auth_user/login.html', context={'form':form})

def logout_request(request):
    logout(request)
    return redirect('/')
