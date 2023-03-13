from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label="Predmet správy: ", max_length=255, required=False)
    email = forms.EmailField(label="Vaša emailová adresa:")
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), label="Vaša správa: ")
