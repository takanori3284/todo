import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = forms.InquiryForm
    success_url = reverse_lazy('diary:index')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries
