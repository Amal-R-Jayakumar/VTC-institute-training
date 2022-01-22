from django.shortcuts import render,redirect
from account.models import User, Profile
from courses.models import Category, Course, Enrollment,TestQuestion
from courses.forms import add_student_form_enroll, add_student_form_profile, add_student_form_user,TestQuestionForm
# Create your views here.

def view_all_courses(request):  # ListCourse Class
    courses = Course.objects.all()
    print (courses)
    return render(request, 'courses.html', {'courses':courses})


def Enrollment_details(request):
    student_user_form = add_student_form_user(None)
    student_profile_form = add_student_form_profile(None)
    student_enrollment_form = add_student_form_enroll(None)
    if request.method == 'POST':
        student_user_form = add_student_form_user(request.POST)
        student_profile_form = add_student_form_profile(request.POST)
        student_enrollment_form = add_student_form_enroll(request.POST)
        print(f'\n\nvalid datas\n\n')
        print(f'\n\n{student_profile_form.cleaned_data}\n\n')
        if student_user_form.is_valid() and student_enrollment_form.is_valid():
            username = student_user_form.cleaned_data.get('email')
            contact_number = student_user_form.cleaned_data.get(
                'contact_number')
            name = student_user_form.cleaned_data.get('name')
            email = student_user_form.cleaned_data.get('email')
            gender = student_user_form.cleaned_data.get('gender')
            qualification = student_profile_form.cleaned_data.get(
                'qualification')
            code = student_profile_form.cleaned_data.get('code', Value="1234")
            mode_of_training = student_enrollment_form.cleaned_data.get(
                'mode_of_training')
            course = student_enrollment_form.cleaned_data.get('course')
            category = student_enrollment_form.cleaned_data.get('category')

            try:
                user = User.objects.create_user(
                    username=username, name=name, contact_number=contact_number, gender=gender, email=email)
                profile = Profile.objects.create(
                    user=user, qualification=qualification, code=code)
                enrollment = Enrollment.objects.create(
                    user=user, mode_of_training=mode_of_training, course=course, category=category)
                return redirect('/home')
            except:
                user = None
        else:
            print(f'\n\nerrors occur\n\n')
    context = {'student_user_form': student_user_form, 'student_profile_form':
               student_profile_form, 'student_enrollment_form': student_enrollment_form}
    return render(request, 'add-student.html', context)


def test_question(request):
    test_form = TestQuestionForm(None)
    if request.method == 'POST':
        test_form = TestQuestionForm(request.POST)
        if test_form.is_valid():
            course = test_form.cleaned_data.get('course')
            question = test_form.cleaned_data.get('question')
            opt1 = test_form.cleaned_data.get('opt1')
            opt2 = test_form.cleaned_data.get('opt2')
            opt3 = test_form.cleaned_data.get('opt3')
            opt4 = test_form.cleaned_data.get('opt4')
            correct_ans = test_form.cleaned_data.get('correct_ans')
            questions = TestQuestion.objects.create(course=course, question=question, opt1=opt1, opt2=opt2, opt3=opt3, opt4=opt4, correct_ans=correct_ans)
            questions.save()
        else:
            print(f'\n\nerror occur\n\n')
    context = {'test_form': test_form}
    return render(request, 'test_question.html', context)
