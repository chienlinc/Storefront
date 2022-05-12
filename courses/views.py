from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Course
from .forms import CourseForm

# Create your views here.

######################################################################

class CourseObjectMixin(object):
    model = Course
    lookup = 'id'

    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id :
            obj = get_object_or_404(self.model, id=id)
        return obj

######################################################################

class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        print(self.queryset)
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list' : self.get_queryset()}
        print(context)
        return render(request, self.template_name, context)

class ChildListView(CourseListView):
    queryset = Course.objects.filter(id=1)

######################################################################

class CourseView(CourseObjectMixin, View):
    template_name = "courses/course_detail.html"

    def get(self, request, id=None, *args, **kwargs):

        # context = {}
        # if id:
        #     obj = get_object_or_404(Course, id=id)
        #     context['object'] = obj
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)

def my_course(request, *args, **kwargs):
    return render(request, 'about.html', {})

######################################################################

class CourseCreateView(View):
    template_name = "courses/course_create.html"

    def get(self, request, *args, **kwargs):
        form = CourseForm()
        context = {"form":form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseForm()

        context = {"form": form}
        return render(request, self.template_name, context)

######################################################################

class CourseUpdateView(CourseObjectMixin, View):
    template_name = "courses/course_update.html"

    # def get_object(self):
    #     id = self.kwargs.get('id')
    #     obj = None
    #     if id :
    #         obj = get_object_or_404(Course, id=id)
    #     return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj:
            form = CourseForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):

        context = {}
        obj = self.get_object()
        if obj:
            form = CourseForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context = {"object":obj, "form":form}
        return render(request, self.template_name, context)

######################################################################

class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html"

    # def get_object(self):
    #     id = self.kwargs.get('id')
    #     obj = None
    #     if id :
    #         obj = get_object_or_404(Course, id=id)
    #     return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):

        context = {}
        obj = self.get_object()
        if obj:
            obj.delete()
            context['object'] = None
            return redirect('../../')
        return render(request, self.template_name, context)


