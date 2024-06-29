from django.shortcuts import render
from testapp.models import employee

# Create your views here.
def employee_view(request):
    employee_list = employee.objects.all()
    # student_list = Student.objects.filter(marks__It=35)
    # student_list = Student.objects.filter(name__startswith='A')
    # student_list = Student.objects.all().order_by('marks')
    # student_list = Student.objects.all().order_by('-marks')
    my_dict = {'employee_list':employee_list}
    return render(request, 'my_app/emp.html', my_dict)


