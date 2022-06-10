from django.shortcuts import render
from .models import User
#from .forms import SignUpForm

def login(request):
    return render(request, 'login.html' )
 
def signup(request):
    if request.method == 'POST': 
        email = request.POST.get('email')
        password = request.POST.get('psw')
        repeat = request.POST.get('psw-repeat')
        #form.save()

        #form = SignupApp(request.POST)
       # test= request.object.all()
        #response = get_response(request) 
        
        print(email, password, repeat)
        return render(request, 'signup.html' )
    else:
         return render(request, 'signup.html' )
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         user.refresh_from_db()  
    #         # load the profile instance created by the signal
    #         user.save()
    #         raw_password = form.cleaned_data.get('password1')
 
    #         # login user after signing up
    #         user = authenticate(username=user.username, password=raw_password)
    #         login(request, user)
 
    #         # redirect user to home page
    #         return redirect('home')
    # else:
    #     form = SignUpForm()
    