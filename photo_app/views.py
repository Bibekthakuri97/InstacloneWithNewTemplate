from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Photomodel,Commentmodel
from user_app.models import UserModel
from .forms import Photoform,Commentform
# Create your views here.
def index(request):
    if 'id' in request.session:
        upload = Photomodel.objects.all()[:10]
        comments = Commentmodel.objects.all()[:20]
        return render(request, 'photo_app/index.html',{'upload': upload, 'comments': comments})
        

    else:
        return redirect('user:login')
    #return HttpResponse('Hello world')

def add(request):
    if request.method == "POST":
        # caption = request.POST.get('caption')
        # photo = request.FILES.get('photo')

        # post = Photomodel()
        # post.save()
        form = Photoform(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('photo_app:index')
            except:
                return HttpResponse('you have failed looser.')

        else:
            print(form.errors)
            return HttpResponse('Form not valid')
    else:
        form = Photoform()
        return render(request,'photo_app/addphoto.html',{'form':form})
 
def edit(request,id):
    photo = Photomodel.objects.get(id=id) #get gives error us filter doesnt, get is used insted of filter
    if request.method == "POST":
        form = Photoform(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            try:
                form.save()
                return redirect('photo_app:index')
            except:
                return HttpResponse('you have failed looser.')

        else:
            print(form.errors)
            return HttpResponse('Form not valid')
    else:
        form = Photoform
        return render(request,'photo_app/editphoto.html',{'photo':photo})
 
def profile(request):
    if 'id' in request.session:
        user_id = request.session['id']
        upload = Photomodel.objects.filter(uploaded_by = user_id)
        user = UserModel.objects.get(id = user_id)
        dict = {'upload':upload,'user':user}
        return render(request, 'photo_app/profile.html',dict)

    else:
        return redirect('user:login')
    
def delete(request,id):
    photo = Photomodel.objects.get(id=id)
    photo.delete()
    return redirect('photo_app:profile')

def search(request):
    if 'id' not in request.session:
        return redirect('user:login')

    userid = request.session.get('id',None)

    if request.method == 'GET':
        query = request.GET.get('q',None)
        
        if query:
            print(query)
            d = {
                    'profiles': UserModel.objects.filter(username__icontains=query).exclude(id=userid),
                    'query': query

            }
            return render(request, 'photo_app/search_result.html',d)
        else:
            return redirect('photo_app:index')
    else:
            return redirect('photo_app:index')