from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import Trainee
from .forms import StudentForm,TraineeForm
# Create your views here.



def create(request): 
    if request.method == 'POST':
        name=request.POST['name']
        intake=request.POST['intake']
        track=request.POST['track']
        bdate=request.POST['bdate']
        obj=Trainee.objects.create(name=name,intake=intake,track=track , bdate=bdate)
        obj.save()
        return redirect(retrieve)
    else:
         return render(request,'create.html')



def retrieve(request):
    current_user = request.session['user']
    param = {'current_user': current_user}
    stds=Trainee.objects.all()
    return render(request,'home.html',{'stds':stds,'current_user':param})


def edit(request,id):
    object=Trainee.objects.get(id=id)
    return render(request,'edit.html',{'object':object})
    
def update(request,id):
    obj=Trainee.objects.get(id=id)
    name=request.POST['name']
    intake=request.POST['intake']
    trake=request.POST['trake']
    bdate=request.POST['bdate']
    obj=Trainee.objects.update(name=name,intake=intake,trake=trake , bdate=bdate)
    obj.save()
    return redirect(retrieve)

def delete(request,id):   
    Trainee.objects.filter(id=id).delete()
    return redirect(retrieve)


def search_trainee(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            stds = Trainee.objects.filter(name__contains=query_name)
            return render(request, 'home.html', {"stds":stds})

    return redirect(retrieve)


def create_Form(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(retrieve)
    else:
         context['form']= form
         return render(request, "create_Form.html", context)

def insertStudent(req):
    context={}
    form=TraineeForm()
    context['form'] = form
    if req.method == 'GET':
        return render(req,'insertStudent.html',context)
    else:
        if(form.is_valid()):
                #server side validation
                form.save()
                return redirect(retrieve)
        else:
            print(form.errors)  
            return render(req,'insertStudent.html',context)
