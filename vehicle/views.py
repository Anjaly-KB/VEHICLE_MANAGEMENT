from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View,FormView,ListView,DetailView,CreateView,UpdateView
from vehicle.models import Vehicles
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
            return redirect("index")
        else:
            return render(request,"add.html",{"form":form})

    # model=Vehicles
    # form_class=VehicleForm
    # template_name: str="add.html"
    # success_url=reverse_lazy("index")

    # def form_valid(self, form):
    #     form.instance.user=self.request.user
    #     return super().form_valid(form)



class VehicleListView(ListView):
    model=Vehicles
    context_object_name="vehicles"
    template_name: str="index.html"

    # def get_queryset(self):
    #     return Vehicles.objects.filter(name=self.request.name)

    def get(self,request,*args,**kwargs):
        vs=Vehicles.objects.all()
        return render(request,"index.html",{"vehicless":vs})
        all_vehicles=vehicles
        return render(request,"index.html",{"vehicles":all_vehicless})

# ---------------------------------------------------------------------------

# class VehicleDeleteView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         Vehicles.objects.filter(id=id).delete()
#         # messages.success(request,"Todo Deleted")
#         return redirect("index")




# class VehicleEditView(UpdateView):
#     model=Vehicles
#     form_class=VehicleForm
#     template_name: str="update.html"
#     pk_url_kwarg: str="id"
#     success_url=reverse_lazy("index")
#     def form_valid(self,form):
#         return super().form_valid(form)
    
