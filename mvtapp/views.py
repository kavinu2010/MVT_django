from django.shortcuts import render,redirect,get_object_or_404
from .models import Model
from .forms import ModelForm
 
# Create your views here.
def home(request):
   model=Model.objects.all()
   return render(request,'home.html',{'model':model})

def create(request):
   if request.method=='POST':
    modelform=ModelForm(request.POST)
    modelform.save()
    return redirect(home)
   
   else:
     modelform=ModelForm()
   return render(request, 'create.html',{'modelform':modelform})

def delete(request, post_id):
  if request.method=='POST':
    deleteform=get_object_or_404(Model, id=post_id)
    deleteform.delete()
    return redirect(home)
  else:
    return redirect(home)


 