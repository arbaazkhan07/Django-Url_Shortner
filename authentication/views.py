from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Register
def userSignup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            uname = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            if (uname and email and password and password2):
                if (password == password2):
                    try:
                        user = User.objects.get(email=email)
                        return render(request, 'auth/signup.html', {'error': 'User already exists.'})
                    except User.DoesNotExist:
                        User.objects.create_user(
                            username=uname,
                            email=email,
                            password=password
                        )
                        messages.success(request, 'Singup successfull, Login here..!')
                        return redirect('login')
                else:
                    return render(request, 'auth/signup.html', {'error': 'Password don\'t match.'})
            else:
                return render(request, 'auth/signup.html', {'error': 'All fields required.'})
        else:
            return render(request, 'auth/signup.html')
    else:
        return redirect('dashboard')
    
# Login
def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            if (email and password):
                try:
                    user = User.objects.get(email=email)
                    auth.login(request, user)
                    messages.success(request, 'Logged in successfully !')
                    return redirect('home')
                except User.DoesNotExist:
                    return render(request, 'auth/login.html', {'error': 'User doesn\'t exists.'})
            else:
                return render(request, 'auth/login.html', {'error': 'All fields required.'})
        else:
            return render(request, 'auth/login.html')
    else:
        return redirect('dashboard')

# Logout
def userLogout(request):
    auth.logout(request)
    return redirect('login')
