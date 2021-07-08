from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegisterForm, UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            form.save() # User saved / registered
            username = form.cleaned_data.get('username')
            # data is stored in cleaned_data dictionary of form class
            messages.success(request, f'Your account has been created! You can now sign in')
            return redirect('login') # go to blog-home
    else:
        form = UserRegisterForm()   
    return render(request,'users/register.html',{'form' : form})
 

@login_required # without login cannot access this page
def profile(request):
    if request.method== 'POST':
        
            
        user_form = UserUpdateForm(request.POST , instance = request.user)
        profile_form  = ProfileUpdateForm(request.POST ,
                        request.FILES ,
                        instance = request.user.profile )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # go to blog-home

    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form  = ProfileUpdateForm(instance = request.user. profile)

    # instance =  request.user --> getting current information 
    # fill all the fields with the current information
     
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,

    }
    return render(request,'users/profile.html',context)  

