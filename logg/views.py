from django.shortcuts import render
from .models import Loggs
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect
from .forms import LoggForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView


def home(request):
    return render(request, 'logg/home.html')


# def logger(request):
#     context = {
#         'Loggs': Loggs.objects.all()
#     }
#     return render(request, 'logg/logger.html', context)


def reminders(request):
    return render(request, 'logg/reminders.html')


class LogCreateView(CreateView):
    template_name = 'logg/log_creation.html'
    form_class = LoggForm
    success_url = reverse_lazy("logg-view")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class LoggListView(ListView):
    model = Loggs
    template_name = 'logg/logg_list_view.html'

    def get_queryset(self):
        return super(LoggListView, self).get_queryset().filter(author=self.request.user)


# class LoggsDeleteView(DeleteView):
#     model = Loggs
#
#     def user_(self):
