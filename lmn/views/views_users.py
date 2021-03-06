from django.shortcuts import render, redirect
from django.contrib import messages

from ..models import Venue, Artist, Note, Show, Profile
from ..forms import VenueSearchForm, NewNoteForm, ArtistSearchForm, UserRegistrationForm, ProfileForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


"""Methods for working with registering new users, accessing current users and login"""
def user_profile(request, user_pk):
    # Get user profile for any user on the site
    user = User.objects.get(pk=user_pk)
    usernotes = Note.objects.filter(user=user.pk).order_by('-posted_date')
    return render(request, 'lmn/users/user_profile.html', { 'user_profile': user , 'notes': usernotes })


""" Edited the logged-in User and directed it to my user profile """
@login_required
def my_user_profile(request):
    
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST, instance=profile) 

        context = {
        'user_form' : form,
        'user_profile': request.user
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            new_user_form = ProfileForm(instance=request.user.profile)
            return redirect('my_user_profile')
        else:
            messages.error(request, form.errors)
            return render(request, 'lmn/users/my_user_profile.html')

        return redirect('my_user_profile')
    else:
        #profile = Note.objects.get(user=request.user)
        profile = Profile.objects.get(user=request.user) 
        star = ""  
        if profile.updatednum_of_user_note:
        
            num = profile.updatednum_of_user_note # user number of notes
            if num >=10: 
                star = "five_star"
            elif num >=8:
                star = "four_star"
            elif num >= 6:
                star ="three_star"
            elif num >= 4:
                star = "two_star"
            elif num >= 1:
                star = "one_star"
            else:
                star = "no_star"
             
        user_form = ProfileForm()
    context = {
        'user_form' : user_form,
        'user_profile': request.user,
        'star': star
    }

    return render(request, 'lmn/users/my_user_profile.html', context)


def register(request):
    """To register a new user"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user:
                login(request, user)
                return redirect('my_user_profile')
            else:
                messages.add_message(request, messages.ERROR, 'Unable to log in new user')
        else:
            messages.add_message(request, messages.INFO, 'Please check the data you entered')
            # include the invalid form, which will have error messages added to it. The error messages will be displayed by the template.
            return render(request, 'registration/register.html', {'form': form} )

    form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form} )

def goodbye(request):
    return render(request, 'registration/logout.html')






    