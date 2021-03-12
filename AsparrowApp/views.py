from django.shortcuts import render
from django.views.generic.base import TemplateView
from AsparrowTech.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from AsparrowApp.forms import EnquiryForm
from AsparrowApp.models import Enqiury
from django.contrib import messages


def home(request):
    return render(request, "index.html",{})

def contact(request):
    form = EnquiryForm()
    if request.method == "POST" :
        #import pdb; pdb.set_trace()
        form  = EnquiryForm(request.POST)
        n = request.POST['name']
        e = request.POST['email']
        p = request.POST['phone']
        m = request.POST['message']
        subject =  n + "  trying to contact  "
        message ="Name : "+ n + ",\n Email : "+ e + ",\n Phone no : "+p +",\n message : "+ m
        recepient = str(form['email'].value())
        send_mail(subject, message, recepient, [EMAIL_HOST_USER], fail_silently = False)
        messages.success(request, "ThankYou For Connecting with Us We will contact you Soon!")
        return render (request, "contact-us.html", {}) 
    return render (request, "contact-us.html", {})
'''
def confirm(request):
    form  = EnquiryForm(request.POST)
    if form.is_valid():
        save_it = form.save(commit= False)
        save_it.save()
        subject = 'AsparrowTech'
        message = save_it
        recepient = str(form['email'].value())
        send_mail(subject, message, recepient, [EMAIL_HOST_USER], fail_silently = False)
        messages.success(request, "ThankYou For Contacting Us")
        return render (request, "contact-us.html", {}) 
    return render (request, "contact-us.html", {})
'''
def services(request):
    return render(request, "services-icon-boxed.html", {})

def about(request):
    return render(request, "about-us.html", {})

def career(request):
    return render(request, "careers.html",{})