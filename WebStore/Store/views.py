from django.shortcuts import redirect, render, get_object_or_404
from .models import kontakt
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateUserForm

# Create your views here.
def index(request):
    context = {}
    if request.POST:
        new_msg = kontakt.objects.create(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], msg=request.POST['msg'])
        new_msg.save()
        return redirect("Store:index")
    return render(request, 'Store/index.html', context)

@login_required(login_url='Store:login')
def account(request):
    return redirect('Store:user', username=request.user)

@login_required(login_url='Store:login')
def user(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user': user}
    return render(request, 'Store/user.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
        else:
            messages.info(request, 'Nazwa uzytkownika lub haslo jest nie prawidlowe')

    context = {}
    return render(request, 'Store/login.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Konto zostało stworzone dla ' + user)

            return redirect('Store:login')

    context = {'form': form}
    return render(request, 'Store/register.html', context)