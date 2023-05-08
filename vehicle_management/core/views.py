from django.shortcuts import render, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import VehicleForm
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Vehicle
from .decorators import auth_user
# Create your views here.

@method_decorator(login_required,name='dispatch')
@method_decorator(auth_user(['SUPER ADMIN']),name='dispatch')
class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = 'core/form.html'
    success_url = "/"
    fields = ['vehicle_number', 'modal', 'description', 'vehicle_option']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context


class VehicleList(ListView):
    model = Vehicle
    template_name = 'core/home.html'

    def get_queryset(self):
        return Vehicle.objects.filter(active_status=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

@method_decorator(login_required,name='dispatch')
@method_decorator(auth_user(['SUPER ADMIN','ADMIN']),name='dispatch')
class VehicleUpdateView(UpdateView):
    model = Vehicle
    template_name = 'core/form.html'
    fields = '__all__'
    success_url = "/"

@method_decorator(login_required,name='dispatch')
@method_decorator(auth_user(['SUPER ADMIN']),name='dispatch')
class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.active_status = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
