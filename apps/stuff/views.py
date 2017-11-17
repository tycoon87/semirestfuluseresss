from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index (request):
    return render(request,'stuff/index.html',{"User": User.objects.all()})

def createUser (request):
    return render(request,'stuff/createUser.html')

def Add(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('stuff/createUser.html')
    else:
        User.objects.create(Firstname=request.POST['Firstname'] , Lastname=request.POST['Lastname'],Email=request.POST['Email'])
        return redirect('/')

def show(request,User_id):
    return render(request, 'stuff/show.html', {"User": User.objects.get(id=User_id)})

def openEdit(request, User_id):

	context = {
	'User': User.objects.get(id=User_id)
	}
	print User_id
	print context
	return render(request, 'stuff/edit.html', {"User": User.objects.get(id=User_id)})

def edit(request,User_id):
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
                return redirect(request, 'stuff/edit.html', {"User": User.objects.get(id=User_id)})
        else:
            u = User.objects.get(id=User_id)
            u.Firstname = request.POST['Firstname']
            u.Lastname = request.POST['Lastname']
            u.Email= request.POST['Email']
            u.save()
        return render(request, 'stuff/show.html', {"User": User.objects.get(id=User_id)})

def delete(request,User_id):
	User.objects.get(id=User_id).delete()
	return redirect('/')
