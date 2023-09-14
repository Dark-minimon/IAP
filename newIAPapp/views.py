from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, MissionForm
from datetime import datetime
from newIAPapp.models import Mission


def me(request):
    missions = Mission.objects.all()
    now = datetime.now()
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'newIAPapp/Личный-кабинет.html', {'user': request.user, 'missions': missions, 'now': now})


def main(request):
    return render(request, 'newIAPapp/main.html')

def delete_mission(request, mission_id):
    mission = Mission.objects.get(pk=mission_id)
    mission.delete()
    return redirect('me')


def update_mission(request, mission_id):
    mission = Mission.objects.get(pk=mission_id)
    form = MissionForm(request.POST or None, instance=mission)
    if form.is_valid():
        form.save()
        return redirect('me')
    return render(request, 'newIAPapp/update_mission.html',
                  {'mission': mission,
                   'form': form})


def userpage(request):
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = MissionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = MissionForm()
    return render(request,
                  'newIAPapp/Главная.html', {
        'user': request.user,
        'missions': Mission.objects.all(),
        'form': form,
        'year': year,
            'month': month,
            'day': day
                  })


def doLogout(request):
    logout(request)
    return redirect('login')


def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('userpage')
            else:
                form.add_error(None, 'Неверные данные!')
    return render(request, 'newIAPapp/login.html', {'form': form})


def registerPage(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    return render(request, 'newIAPapp/registration.html', {'form': form})
