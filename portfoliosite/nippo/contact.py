from django.shortcuts import redirect, render
from django.urls import reverse
# from django.utils import email_set

def contactView(request):
    template_name = "contact.html"
    if request.POST:
        # email_set.contactFromNippo(request.POST)
        return redirect(reverse("nippo-contact"))

    return render(request, template_name)