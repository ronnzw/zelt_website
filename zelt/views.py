from __future__ import absolute_import
from django.shortcuts import render, reverse, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages
from datetime import datetime


from .forms import ContactForm



def home(request):
    return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

def our_products(request):
	return render(request, 'our_products.html', {})

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['rmaravanyika@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "contact.html", {'form': form})
'''
def contact(request):
    # check captcha
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            # process the data in contact_form.cleaned_data as required
            obj = Contact()  # gets new object
            obj.name = contact_form.cleaned_data['name']
            obj.company = contact_form.cleaned_data['company']
            obj.email = contact_form.cleaned_data['email']
            obj.message = contact_form.cleaned_data['message']
            # finally save the object in db
            obj.save()

            # send email to rmaravanyika@gmail.com
            subject = "Message on Zelt website Contact Form "
            message = 'A message was submitted on the website\n\n'
            message += 'Name: ' + contact_form.cleaned_data['name'] + '\n'
            message += 'Email: ' + contact_form.cleaned_data['email'] + '\n'
            message += 'Company: ' + contact_form.cleaned_data['company'] + '\n'
            message += 'Message:\n ' + contact_form.cleaned_data['message'] + '\n'

            sender = 'rmaravanyika@zimbopy.com'

            recipient_list = ['rmaravanyika@gmail.com']
            send_mail(subject, message, sender, recipient_list)

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('/thanks'))
        
    else:
        # if a GET (or any other method) we'll create a blank form
        contact_form = ContactForm()

        return HttpResponseRedirect(reverse('contact')) '''


"""Renders the thanks page"""
def thanks(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'thanks.html',
        {
            'title': 'Message Sent ',
            'message': 'Message sent ',
            'year': datetime.now().year,
        }
    )
# Create your views here.

# Create your views here.
