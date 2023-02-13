from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    return render(request, 'aviation_school/home.html')

def become_pilot(request):
    return render(request, 'aviation_school/become_a_pilot.html')

def sightseeing_tour(request):
    return render(request, 'aviation_school/sightseeing_tour.html')

def our_aircraft(request):
    return render(request, 'aviation_school/our_aircraft.html')

def book_flight(request):
    sent = False
    message = request.GET.get('message', '')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['name']} has a request about Top Air."
            message = f"{cd['name']} has a question/ wants to book a flight" \
                      f"Email: {cd['email']}"\
                      f"Phone number: {cd['phone']}"\
                      f"Message : {cd['message']}"
            send_mail(subject, message, cd['email'],
                      ['alexander.gospodinov2003@gmail.com'])
            sent = True
    else:
        form = ContactForm(initial={'message': message})
    return render(request, 'aviation_school/book_flight.html', {'form': form, 'sent': sent})






