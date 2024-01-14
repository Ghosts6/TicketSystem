from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.http import FileResponse
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import TicketForm
from .models import Ticket
from django.contrib import messages
from .forms import TicketForm 
import os

def home(request):
    return render(request, 'home.html')

def user_login(request):
    error_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            error_message = 'Fill in all the necessary data'
        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin:index')
                else:
                    return redirect('main')
            else:
                try:
                    failed_login_user = User.objects.get(username=username)
                    failed_login_user.profile.failed_login_attempts += 1
                    failed_login_user.profile.last_login_attempt = timezone.now()
                    failed_login_user.profile.save()

                    if failed_login_user.profile.failed_login_attempts > 10:
                        lock_time = failed_login_user.profile.last_login_attempt + timedelta(minutes=5)
                        if timezone.now() < lock_time:
                            return render(request, 'locked.html')
                        else:
                            failed_login_user.profile.failed_login_attempts = 0
                            failed_login_user.profile.save()
                except User.DoesNotExist:
                    pass  
                
                error_message = 'Incorrect password or username'

    return render(request, 'login.html', {'error': error_message})

def main(request):
    if request.method == 'POST':
        # Set the status field
        request.POST = request.POST.copy()
        request.POST['status'] = 'Pending'

        form = TicketForm(request.POST, request.FILES)  

        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['last_name']
            department = form.cleaned_data['department_name']
            request_type = form.cleaned_data['request_type']  
            description = form.cleaned_data['description']
            attachment = request.FILES.get('attachment')

            ticket = Ticket(
                user=request.user,
                name=name,
                last_name=lastname,
                department_name=department,
                request_type=request_type,
                description=description,
                attachment=attachment,
                status='Pending',  
            )
            ticket.save()

            return redirect('status')  
    else:
        form = TicketForm()

    return render(request, 'main.html', {'form': form})

def locked(request):
    return render(request, 'locked.html')

def status(request):
    if request.user.is_authenticated:
        user_tickets = Ticket.objects.filter(user=request.user)
        return render(request, 'status.html', {'user_tickets': user_tickets})
    else:

        return render(request, 'home.html')

def admin_panel(request):
    all_tickets = Ticket.objects.order_by('name')
    return render(request, 'admin_panel.html', {'all_tickets': all_tickets})
