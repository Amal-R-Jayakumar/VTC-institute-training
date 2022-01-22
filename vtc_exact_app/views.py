from django.shortcuts import render
from vtc_exact_app.models import Batch
from vtc_exact_app.forms import BatchForm
from courses.models import Course,TestQuestion

# Create your views here.
def add_batch(request):
    batch_fill_form = BatchForm(None)
    if request.method == 'POST':
        batch_fill_form = BatchForm(request.POST)
        if batch_fill_form.is_valid():
            batch_no = batch_fill_form.cleaned_data.get('batch_no')
            max_no_of_students = batch_fill_form.cleaned_data.get('max_no_of_students')
            user = request.user
            print(user)
            batch = Batch.objects.create(
                batch_no=batch_no, max_no_of_students=max_no_of_students, user=user)
            batch.save()
    context = {'form': batch_fill_form}
    return render(request, 'add-batch.html',context)
def show_test_questions(request):
    courses = Course.objects.all()
    return render(request,'view-test-questions-by-vtc.html',{'courses':courses})
def show_questions_by_course(request,id):
    data = Course.objects.get(id=id)
    print(data)
    qs = TestQuestion.objects.filter(course_id__id=data.id)
    print(qs)
    context={'data':data, 'qs':qs}
    return render(request, 'view-test-questions-by-category.html',context)