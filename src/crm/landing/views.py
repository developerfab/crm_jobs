from django.shortcuts import render
from django.http import HttpResponse
from forms import ContactUserForm


# Create your views here.
def home(request):
    f = ContactUserForm()
    return render(request, "home.html", {"form": f})


def faq(request):
    return render(request, "faq.html")


def contact_me(request):
    if request.POST:
        f = ContactUserForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse('{"status": "OK"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "ERROR"}', content_type='application/json', status=400)
    return HttpResponse('{"status": "ERROR"}', content_type='application/json', status=403)