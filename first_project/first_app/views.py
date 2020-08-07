from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from first_app.models import Topic, Webpage, AccessRecord
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}
    my_dict = {'insert_me':"Hello I am from view.py!!!"}
    return render(request, "first_app/index.html", context=date_dict)

def form_name_view(request):
    form = forms.NewWebpageForm()
    if request.method == 'POST':
        form = forms.NewWebpageForm(request.POST)

        if form.is_valid():
            # Do something code
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')
    return render(request, 'first_app/index.html', {'form' : form})

def register(request):
    registered = False

    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'first_app/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,

    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login and failed')
            print("Username: {} and password {}".format(username, pasword))
            return HttpResponse('invalid login details supplied')
    else:
        return render(request, 'first_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('You are logged in. Nice.')
