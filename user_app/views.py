from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserModel
from .forms import RegisterForm

# Create your views here.
def display(request):
    return render(request, 'user_app/display.html')

def logout(request):
    request.session.flush()
    return redirect('user:login')

def loginauth(request):

    if request.method == "POST":
        e = request.POST.get('email')
        pw = request.POST.get('pass')

        user = UserModel.objects.filter(email=e,passwrod=pw)

        if(user.count()>0):
            for user in user:
                request.session['email'] = user.email
                request.session['id'] = user.id
                request.session['username'] = user.username
                return redirect('photo_app:index')

        else:
            return HttpResponse('Milenaaaaa')

    else:    
        return render(request, 'user_app/login.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('user:login')
            except:
                return HttpResponse('Cannot be registerred')
        else:
            return HttpResponse('not valid form')
    else:
        form = RegisterForm()
        return render(request, 'user_app/register.html',{'form':form})
        # return HttpResponse('error')