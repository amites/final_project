from django.http import HttpResponse
from django.shortcuts import render

from fitness.forms import BMIForm, WorkoutForm
from fitness.models import UserBMIProfile



def bmi_view(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BMIForm()
    objs = UserBMIProfile.objects.all()
    thing = UserBMIProfile.objects.get(id=9) #request.user.id - connect user model to profile model
    context = {
        'objs': objs,
        'thing': thing,
        'form': form,
    }
    return render(request, 'base.html', context)


def workout_view(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WorkoutForm
        context = {'form': form}
        return render(request, 'wotemp.html', context)





"""
def home_view(request):
    return render(request, 'home.html')


def dashboard(request):
    context = {'html': 'THIS IS MY NEW CODE!'}
    return render(request, 'menu_sidebar.html')




def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_deta)
            login(new_user)
            return HttpResponseRedirect('main.html')
    else:
        form = UserForm()
    return render(request, 'adduser.html', {'form' : form})

"""

