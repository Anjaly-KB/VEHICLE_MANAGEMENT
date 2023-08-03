from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View,FormView,ListView,DetailView,CreateView,UpdateView
from vehicle.models import Vehicles
from django.contrib import messages
from vehicle.forms import RegistrationForm,LoginForm,VehicleForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout



class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")


class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"
    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                # print("SUCCESS")
                return redirect("index")
            else:
                messages.error(request,"INVALID CREDENTIALS")
                return render(request,self.template_name,{"form":form})



class VehicleCreateView(View):
    def get(self,request,*args,**kwargs):
        form=VehicleForm()
        return render(request,"add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=VehicleForm(request.POST)
        if form.is_valid():
            v_name=form.cleaned_data.get("name")
            v_number=form.cleaned_data.get("number")
            v_type=form.cleaned_data.get("type")
            v_model=form.cleaned_data.get("model")
            v_description=form.cleaned_data.get("description")
            Vehicles.objects.create(name=v_name,number=v_number,type=v_type,model=v_model,description=v_description)
            messages.success(self.request,"Vehicle has been added")
            return redirect("index")
        else:
            return render(request,"add.html",{"form":form})



class VehicleListView(ListView):
    model=Vehicles
    context_object_name="vehicles"
    template_name: str="index.html"

    def get_queryset(self):
        return Vehicles.objects.all()

    

class VehicleDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Vehicles.objects.filter(id=id).delete()
        messages.success(request,"vehicle Deleted")
        return redirect("index")




class VehicleEditView(UpdateView):
    model=Vehicles
    form_class=VehicleForm
    template_name: str="update.html"
    pk_url_kwarg: str="id"
    success_url=reverse_lazy("index")
    def form_valid(self,form):
        messages.success(self.request,"Vehicle Updated")
        return super().form_valid(form)
    



def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            messages.error(request,"u must login to continue")
            return redirect("signin")
        else:
            return fn(request,*args,**kw)
    return wrapper

@signin_required
def signout(request,*args,**kw):
    logout(request)
    return redirect("signin")