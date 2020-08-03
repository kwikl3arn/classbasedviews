from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)
from basic_app.models import School, Student


#  Function View:
# def index(request):
#     return render(request,'index.html')


# class function view
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

    # to send any data by useing context we need to define this function
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context


class SchoolListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    model = School


class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    # specify fields that you want to show from models
    fields = ("name", "principal", "location")
    # if you want to show all fields from models,use below one
    # fields = "__all__"
    model = School


class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = School


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("list")


class CBView(View):
    def get(self, request):
        return HttpResponse('Class Based Views are Cool!')
