from django.contrib import admin
from testapp.models import employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','dob','marks','email','phonenumber','address']
admin.site.register(employee,EmployeeAdmin)


