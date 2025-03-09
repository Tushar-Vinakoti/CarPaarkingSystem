from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Vehicle
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime

@ensure_csrf_cookie
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'parking/login.html')

@login_required(login_url='login')
@ensure_csrf_cookie
def dashboard(request):
    return render(request, 'parking/dashboard.html')

@login_required(login_url='login')
@ensure_csrf_cookie
def add_vehicle(request):
    if request.method == 'POST':
        try:
            # Parse datetime strings to datetime objects
            entry_time = datetime.strptime(request.POST.get('entry_time'), '%Y-%m-%d %H:%M')
            exit_time = datetime.strptime(request.POST.get('exit_time'), '%Y-%m-%d %H:%M')
            
            # Create new vehicle
            vehicle = Vehicle.objects.create(
                owner=request.user,
                owner_name=request.POST.get('owner_name'),
                phone_number=request.POST.get('phone_number'),
                vehicle_number=request.POST.get('vehicle_number'),
                registration_number=request.POST.get('registration_number'),
                vehicle_type=request.POST.get('vehicle_type'),
                entry_time=entry_time,
                exit_time=exit_time
            )
            messages.success(request, 'Vehicle registered successfully!')
            return redirect('view_vehicles')
        except Exception as e:
            messages.error(request, f'Error registering vehicle: {str(e)}')
    
    return render(request, 'parking/add_vehicle.html')

@login_required(login_url='login')
@ensure_csrf_cookie
def view_vehicles(request):
    vehicles = Vehicle.objects.filter(owner=request.user)
    return render(request, 'parking/view_vehicles.html', {'vehicles': vehicles})

@login_required(login_url='login')
@ensure_csrf_cookie
def payment(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, owner=request.user)
    
    if request.method == 'POST':
        try:
            # Process payment (fake)
            vehicle.delete()
            messages.success(request, 'Payment successful! Vehicle has been checked out.')
            return redirect('view_vehicles')
        except Exception as e:
            messages.error(request, f'Error processing payment: {str(e)}')
    
    return render(request, 'parking/payment.html', {'vehicle': vehicle})

def logout_view(request):
    logout(request)
    return redirect('login')