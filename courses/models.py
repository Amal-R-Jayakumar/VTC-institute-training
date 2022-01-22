from django.db import models
from account.models import User, Profile
from vtc_exact_app.models import VtcModel, Batch
#from account.models import User, Profile

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=60)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    slug = models.SlugField(default='', max_length=255, editable=False)
    course_description = models.TextField()
    course_image = models.ImageField(
        upload_to='images/course_images', default='images/default.png')
    completion_time = models.DurationField()
    rating = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.course_name

class Enrollment(models.Model):
    MODE_OF_TRAIN_CHOICES = (
        (1, 'Offline'), (2, 'Online')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mode_of_training = models.PositiveIntegerField(
        choices=MODE_OF_TRAIN_CHOICES, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    study_center = models.ForeignKey(VtcModel,on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.user}\'s Enrollment details'

    class Meta:
        unique_together = ('course', 'user')


class TestQuestion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=400)
    opt1 = models.CharField(max_length=100)
    opt2 = models.CharField(max_length=100)
    opt3 = models.CharField(max_length=100)
    opt4 = models.CharField(max_length=100)
    correct_ans = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.question}'
