from django.contrib import messages
from django.shortcuts import redirect, render
from random import randint
from .forms import NippoFormClass, InquiryForm
from django.urls import reverse
from django.views import generic
# from django.utils import email_set
import logging
from django.urls import reverse_lazy
logger = logging.getLogger(__name__)

def nippoListView(request):
    return render(request,
                  "nippo/nippo-list.html")

def nippoDetailView(request, number):
    template_name="nippo/nippo-detail.html"
    random_int = randint(1,10)
    ctx = {
        "random_number": random_int,
        "number": number,
    }
    return render(request, template_name, ctx)


def nippoCreateView(request):
    template_name="nippo/nippo-form.html"
    form = NippoFormClass()
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def contactView(request):
    template_name = "nippo/contact.html"
    if request.POST:
        # email_set.contactFromNippo(request.POST)
        return redirect(reverse("nippo-contact"))

    return render(request, template_name)

class IndexView(generic.TemplateView):
    template_name = "inquiry.html"
    form_class = InquiryForm

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('nippo:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
    