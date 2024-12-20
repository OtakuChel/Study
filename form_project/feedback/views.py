from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views import View
# Create your views here.

#class FeedbackView(View):
#
#    def get(self, request):
#        form = FeedbackForm()
#        return render(request, 'feedback/feedback.html', context={'form': form})
#
#    def post(self, request):
#        form = FeedbackForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/done')
#        return render(request, 'feedback/feedback.html', context={'form': form})

#class FeedBackUpdateView(View):
#
#    def get(self, request, id_feedback: int):
#        feed = Feedback.objects.get(id=id_feedback)
#        form = FeedbackForm(instance=feed)
#        return render(request, 'feedback/feedback.html', context={'form': form})
#
#
#    def post(self, request, id_feedback: int):
#        feed = Feedback.objects.get(id=id_feedback)
#        form = FeedbackForm(request.POST, instance=feed)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/done')
#        return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(TemplateView):r
    template_name = 'feedback/done.html'

#class ListFeedBack(TemplateView):
#    template_name = 'feedback/list_feedback.html'
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['feedbacks'] = Feedback.objects.all()
#        return context

#class DetailFeedBack(TemplateView):
#    template_name = 'feedback/detail_feedback.html'
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['feedback'] = Feedback.objects.get(id=kwargs['id_feedback'])
#        return context

class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(rating__gt=4)
        return  filter_qs

class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback


#class FeedbackView(FormView):
#    form_class = FeedbackForm
#    template_name = 'feedback/feedback.html'
#    success_url = '/done'
#
#    def form_valid(self, form):
#        form.save()
#        return super(FeedbackView, self).form_valid(form)


class FeedbackView(CreateView):
    model = Feedback
    #fields = '__all__'
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

class FeedBackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm #То, как будет выглядеть форма
    template_name = 'feedback/feedback.html'
    success_url = '/done'
