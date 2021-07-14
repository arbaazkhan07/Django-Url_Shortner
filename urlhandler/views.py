from hashlib import new
from django.contrib.messages.api import warning
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Shorturl
import random, string

# Home
@login_required(login_url='/login/')
def home(request, short_url=None):
    if not short_url or short_url is None:
        return render(request, 'urls/home.html')
    else:
        try:
            check = Shorturl.objects.get(short_query=short_url)
            check.visits = check.visits + 1
            check.save()
            original_url = check.original_url
            return redirect(original_url)
        except Shorturl.DoesNotExist:
            return render(request, 'urls/home.html', {'error': 'Oops! Somthing went wrong.'})

#Dashboard
@login_required(login_url='/login/')
def dashboard(request):
    user = request.user
    urls = Shorturl.objects.filter(user=user)
    return render(request, 'urls/dashboard.html', {'urls': urls})

def randomGen():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

@login_required(login_url='/login/')
def generater(request):
    if request.method == 'POST':
        user = request.user
        original = request.POST['original']
        short = request.POST['short']

        if original and short:
            check = Shorturl.objects.filter(short_query=short)
            if not check:
                newUrl = Shorturl( user=user, original_url=original, short_query=short )
                newUrl.save()
                return redirect('dashboard')
            else:
                messages.error(request, 'Url already exists.')
                return redirect('dashboard')
        elif original:
            generated = False
            while not generated:
                short = randomGen()
                check = Shorturl.objects.filter(short_query=short)
                if not check:
                    newUrl = Shorturl(user=user, original_url=original, short_query=short)
                    newUrl.save()
                    return redirect('dashboard')
                else:
                    continue
        else:
            messages.error(request, 'All fields required.')
            return redirect('dashboard')
    else:
        return redirect('dashboard')
