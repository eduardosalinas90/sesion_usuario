from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistroForm, ContactForm
from .models import Registrado

# Create your views here.

def home(request):
    return render(request, "home.html",{})

def RegistroUsuario(request):
    form = RegistroForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():

        instance = form.save(commit = False)
        context = {'titulo':'Gracias %s' % (instance.nombre)}
        if not instance.nombre:
            instance.nombre = "NomDefecto"
            context = {'titulo':'Gracias %s' % (instance.email)}
        instance.save()

    return render(request, "inicio.html",context)

def contact(request):

    form = ContactForm(request.POST or None)
    context = {'form':form}

    if form.is_valid():
        form_data = form.cleaned_data
        form_nombre = form_data.get("nombre")
        form_email = form_data.get("email")
        form_mensaje = form_data.get("mensaje")
        form_asunto = form_data.get("asunto")
        form_mensaje = ' Te escribio esta persona %s y su correo es %s y este es su mensaje %s' %(form_nombre, form_email, form_mensaje)

        email_from = settings.EMAIL_HOST_USER
        email_to = ["juman_20002@hotmail.com"]

        if send_mail(form_asunto, form_mensaje, email_from,email_to, fail_silently = False):
            context = {'mensaje':'Mensaje enviado'}

    return render(request, 'form_contact.html',context)


