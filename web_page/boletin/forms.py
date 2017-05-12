from django import forms
from .models import Registrado

class RegistroForm(forms.ModelForm):

    class Meta:

        model = Registrado

        fields = ["nombre","email",]
        labels = {
            'nombre':'Nombre',
            'email': 'Email',
        }

        widgets = {

            'nombre':forms.TextInput(),
            'email': forms.TextInput(),

        }


    def clean_email(self):

        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")

        if not extension == 'edu':
            raise forms.ValidationError ('La extension del correo debe ser .EDU')

        return email

class ContactForm(forms.Form):

    nombre = forms.CharField(widget= forms.TextInput())
    email = forms.EmailField(widget= forms.TextInput())
    asunto = forms.CharField(widget= forms.TextInput())
    mensaje = forms.CharField(widget= forms.Textarea)

