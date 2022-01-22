from django.shortcuts import render
from affiliation.models import Affiliation_inspection, Affiliation_request
from affiliation.forms import affiliation_request_form, affiliation_inspection_form
from account.views import home_view
import random
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def Affiliation_first_form(request):
    form = affiliation_request_form()
    if request.method == 'POST':
        form = affiliation_request_form(request.POST)
        if form.is_valid():

            owner_name = form.cleaned_data.get('owner_name')
            email = form.cleaned_data.get('email')
            contact_number = form.cleaned_data.get('contact_number')
            location = form.cleaned_data.get('location')
            localbodytype = form.cleaned_data.get('localbodytype')
            localbodyname = form.cleaned_data.get('localbodyname')
            district = form.cleaned_data.get('district')
            pincode = form.cleaned_data.get('pincode')
            # district = form.cleaned_data.get('district')
            # corporation = form.cleaned_data.get('corporation')
            # municipality = form.cleaned_data.get('municipality')
            # panchayath = form.cleaned_data.get('panchayath')
            # token = Affiliation_request.objects.make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

            # password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz01234567889"
            # length = int(24)
            # token = "".join(random.sample(password,length))
            # print(token)
            if not Affiliation_request.objects.filter(email=email):
                details = Affiliation_request.objects.create(owner_name=owner_name, email=email,
                                                             contact_number=contact_number, location=location,
                                                             localbodytype=localbodytype, localbodyname=localbodyname,
                                                             district=district, )
                details.save()
                # subject = 'welcome to VIJAYAVEEDHI'
                # message = f'Thanks for giving interest for VTC. Please follow the link for further procedures. {password} thank you '
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [details.email, ]
                # send_mail(subject, message, email_from, recipient_list)
                # return redirect('home')
            else:
                form.add_error(error="User already exists", field="email")
    return render(request, 'affiliation.html', {'form': form})


def view_new_affiliation(request):
    data = Affiliation_request.objects.all()

    return render(request, 'affiliation_requests_1.html', {'datas': data})


def accepting_vtc_first(request, id):
    data = Affiliation_request.objects.get(id=id)
    print("im working")
    password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz"
    length = int(24)
    token = "".join(random.sample(password, length))
    data.token = token
    data.save()
    subject = 'welcome to VIJAYAVEEDHI'
    message = f'Thanks for giving interest for VTC. Please follow the link for further procedures. thank you http://127.0.0.1:8000/secondform/?{token} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [data.email, ]
    send_mail(subject, message, email_from, recipient_list)
    # return render(request, 'affiliation_form_2.html',{'result':data})
    return render(request, 'affiliation_requests_1.html')


def affiliation_second(request):
    temp_url = request.get_full_path
    new_val = str(temp_url)
    print(type(new_val))
    print(new_val[-27:-3])
    actual_value = new_val[-27:-3]
    # obj = Affiliation_request.objects.get(id=7)
    obj = Affiliation_request.objects.get(token=actual_value)
    val = obj.token
    print(val)
    print(obj.owner_name)
    print(type(obj.token))
    if val in actual_value:
        print("token match")
    else:
        print("not match")
    return render(request, 'vtc-inspection.html', {'obj': obj})


def accepting_vtc_second(request, id):
    data = Affiliation_inspection.objects.get(id=id)
    print("im working")
    password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz"
    length = int(24)
    token = "".join(random.sample(password, length))
    data.token = token
    data.save()
    subject = 'welcome to VIJAYAVEEDHI'
    message = f'Thanks for giving interest for VTC. Please follow the link for further procedures. thank you http://127.0.0.1:8000/thirdform/?{token} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [data.email, ]
    send_mail(subject, message, email_from, recipient_list)
    # return render(request, 'affiliation_form_2.html',{'result':data})
    return render(request, 'vtc-inspection.html')
