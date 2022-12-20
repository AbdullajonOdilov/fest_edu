from django.db import models

# Create your models here.

class EduUser(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(opload_to="edu/", blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self): return self.name

#Teachers
class Teacher(models.Model):
    edu_id = models.ForeignKey(EduUser, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=100)
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(opload_to="teacher/", blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self): return self.full_name

#Students
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(opload_to="student/", blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self): return self.full_name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    edu_id = models.ForeignKey(EduUser, on_delete=models.CASCADE)
    student_id = models.ManyToManyField(Student)
    date = models.DateField(auto_now_add=True)


    def __str__(self):return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    desc = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    max_ball = models.PositiveSmallIntegerField(default=5)
    type = models.CharField(max_length=10, choices=(('T','Test'), ('F', 'File')))
    def __str__(self): return self.name


class File(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='task/')
    date = models.DateField(auto_now_add=True)


class Tests(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    duration = models.TimeField()


class Test(models.Model):
    matter = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    error1 = models.CharField(max_length=255)
    error2 = models.CharField(max_length=255)
    error3 = models.CharField(max_length=255)
    def __str__(self): return self.id

#Toshiriqlarni tekshirish u-n ishlanganlarga

class DoneTask(models.Model):
    user_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=(('T', 'Test'), ('F', 'File')))

class DoneFile(models.Model):
    task_id = models.ForeignKey(DoneTask, on_delete=models.CASCADE)
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)
    comment = models.CharField(max_length=222)
    ball = models.PositiveSmallIntegerField(default=0)
    date = models.DateField(auto_now_add=True)


class DoneTests(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    done_task_id = models.ForeignKey(DoneTask, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    ball = models.PositiveSmallIntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DataTimeField()


class DoneTest(models.Model):
    done_test_id = models.ForeignKey(DoneTests, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Tests, on_delete=models.CASCADE)
    chose = models.BooleanField(default=False)