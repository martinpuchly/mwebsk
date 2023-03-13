from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .form import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            contact = Contact.objects.create(
                subject = subject,
                email = email,
                message = message
            )
            messages.success(request, 'Správa bola odoslaná. Ďakujem.')
            return redirect('contact')      
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})