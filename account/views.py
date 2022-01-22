from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from account.models import Enquiryform, User, Profile
from django.contrib.auth import authenticate, login
from account.forms import UserSignUpForm, SignupProfileForm, UserLoginForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
import re
from django.contrib import messages


def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """

    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


def home_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        PostData = request.POST
        fname = PostData.get('fname')
        email = PostData.get('email')
        phone_code = PostData.get('phone_code')
        mobile_number = PostData.get('mobile_number')
        course_interested = PostData.get('course_interested')
        place_of_study = PostData.get('place_of_study')
        # validation
        error_message = None
        if fname.isdigit():
            error_message = "Please enter valid name"
        if len(mobile_number) != 10:
            error_message = "Please enter correct Phone number"
        if not error_message:
            enquiry = Enquiryform(fname=fname, email=email, phone_code=phone_code, mobile_number=mobile_number,
                                  course_interested=course_interested, place_of_study=place_of_study)
            enquiry.register()
        logged_in = request.user.is_authenticated
        user = request.user
        context = {'logged_in': logged_in,
                   'user': user,
                   'error_message': error_message,
                   }
        return render(request, 'index.html', context)


def signup(request):
    sign_up_form = UserSignUpForm(None)
    profile_form = SignupProfileForm(None)
    if request.method == 'POST':
        sign_up_form = UserSignUpForm(request.POST)
        profile_form = SignupProfileForm(request.POST)
        print(f'\n\nvalid datas\n\n')
        if sign_up_form.is_valid() and profile_form.is_valid():
            username = sign_up_form.cleaned_data.get('email')
            contact_number = sign_up_form.cleaned_data.get('contact_number')
            name = sign_up_form.cleaned_data.get('name')
            email = sign_up_form.cleaned_data.get('email')
            gender = sign_up_form.cleaned_data.get('gender')
            dob = profile_form.cleaned_data.get('dob')
            address = profile_form.cleaned_data.get('address')
            qualification = profile_form.cleaned_data.get('qualification')
            # print(f'\n\n{dob}\n{address}\n{qualification}\n\n')
            # print(f'\n\n{profile_form}\n\n')
            password1 = sign_up_form.cleaned_data.get('password1')
            password2 = sign_up_form.cleaned_data.get('password2')

            if password1 != password2:
                sign_up_form.add_error(field='password2',
                                       error='Passwords Do Not Match')
            else:
                try:
                    user = User.objects.create_user(username=username, name=name, contact_number=contact_number,
                                                    gender=gender, email=email, password=password1)
                    profile = Profile.objects.create(user=user, dob=dob, address=address, qualification=qualification)
                except:
                    user = None
                if user != None:
                    login(request, user)
                    profile.save()
                    return redirect('login')
                else:
                    request.session['register_error'] = 1
        if sign_up_form.errors:
            print(f'\n\n{sign_up_form.errors}\n\n')
        else:
            print(f'\n\nno errors\n\n')
    context = {'sign_up_form': sign_up_form, 'profile_form': profile_form}
    return render(request, 'signup.html', context)


def login_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        # next = request.user.get('next')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # if user.is_active:
            login(request, user)
            # else:
            #     messages.warning('Your account is deactivated')
            return redirect('view_profile')

    context = {'title': 'IT Kerala | Login', 'form': form, }
    return render(request, 'login.html', context)


@login_required
def view_profile(request):
    return render(request, 'viewprofile.html')


def about_vijayaveedhi(request):
    return render(request, 'about-vijayaveedhi.html')


def about_rutronix(request):
    return render(request, 'about-rutronix.html')


def contact(request):
    return render(request, 'contact.html')


def vtc(request):
    return render(request, 'vtc.html')


# def edit_profile(request):
#     user = request.user
#     data = Profile.objects.filter(user_id=current_user.id)
#     data_user = User.objects.filter(id=current_user.id)
#     print(data)
#     print(data_user)
#     form = profileUpdateForm(None)

#     if request.method == 'POST':
#         form = profileUpdateForm(request.POST)
#         if form.is_valid():
#             dob = form.cleaned_data.get('dob')
#             address = form.cleaned_data.get('address')
#             qualification = form.cleaned_data.get('qualification')
#             try:
#                 profile = Profile.objects.create(dob=dob, address=address, qualification=qualification)
#             except:
#                 user = None
#             if user != None:
#                 profile.save()
#     context = {'data':data, 'form':form, 'data_user':data_user,}
#     return render(request,'edit-profile.html',context)

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, instance=user)
        if request.user.user_type == 1:
            u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            gender = u_form.cleaned_data.get('gender')
            dob = p_form.cleaned_data.get('dob')
            address = p_form.cleaned_data.get('address')
            user_save = u_form.save(commit=False)
            user_save.user = request.user
            user_save.save()
            profile_save = p_form.save(commit=False)
            profile_save.user = request.user
            profile_save.save()
            # profile_submission.save()
            messages.success(request, 'Your account has been successfully updated!')
            # return redirect('courses:courses')
            return redirect('view_profile')
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user,
        # 'profile': profile,
    }
    return render(request, 'edit-profile.html', context)