from django.shortcuts import render, redirect
from Email_Verify.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def login(request):
    return render(request, 'Email/login.html',)
@csrf_exempt
def register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password, email)
        
        try:
            if User.objects.filter(username=username).first():
                messages.success(request,'Username or email may be same')
                return redirect('register')
           
            user_obj=User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
        
            auth_token=str(uuid.uuid4())
            profile_obj=Profile.objects.create(user= user_obj , auth_token= auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)
            return redirect('token')
        except Exception as e:
            print(e)
            
    return render(request, 'Email/register.html',)


def success(request):
    return render(request, 'Email/success.html')

def token(request):
    return render(request, 'Email/token.html')

def error(request):
    return render(request, 'Email/error.html')

def verify(request, auth_token):  # sourcery skip: use-named-expression
    try:
        profile_obj= Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            profile_obj.is_verified=True
            profile_obj.save()
            messages.success(request, "Your account has been verified")
            return redirect('login')
        else:
            return redirect('error')
    
    except Exception as e:
          print(e)      
        
        
def send_mail_after_registration(email, token):
    subject="Your account need too verify"
    messages= f'Hi, please click on this link for account http://127.0.0.1:8000/Email/verify/{token}'
    email_from = "abajmal211@gmail.com"
    recipient_list = [email]
    print (send_mail(subject, messages ,email_from, recipient_list ))