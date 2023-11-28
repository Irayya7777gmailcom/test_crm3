from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.models import User
from Administrator.models import UserProfile
from django.contrib.auth import logout




def main_login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            desig = UserProfile.objects.get(user=user).designation
            print(desig)
            if desig == 'manager':
                dj_login(request, user)
                return redirect('manager-home')             
            elif desig == 'councellor':
                 
                 dj_login(request, user)
                 return redirect('councellor_home')
            elif desig == 'admin':
                 dj_login(request, user)
                 return redirect('adminstrator_home')
            elif desig == 'telecaller':
                 dj_login(request, user)
                 return redirect('tellecaller-home')
            
            else:
                messages.error(request, f"Welcome, {desig}! Redirect to your home page.")
                return HttpResponse(f"Welcome, {desig}! Redirect to your home page.")

        else:
            print(user)
            messages.error(request, "Invalid username or password.")
            return redirect("/")
    
    else:
        return render(request, 'crm_template/Login_page.html')

def logout_view(request):
    logout(request)
    return redirect('/')


