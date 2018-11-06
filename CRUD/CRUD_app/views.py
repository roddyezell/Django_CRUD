from django.shortcuts import render
from CRUD_app.forms import NewUser
from CRUD_app.models import User

# Create your views here.
def index(request):
    return render(request, 'CRUD_app/index.html')

def newuser(request):

    form = NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)
    
        if form.is_valid():
            form.save(commit=True)
            return showusers(request)
        else:
            print('ERROR')
    return render(request, 'CRUD_app/newuser.html',{'form':form})

def showusers(request):

    user_list = User.objects.order_by('username')
    user_dict = {"users":user_list}
    return render(request, 'CRUD_app/showusers.html',context=user_dict)
