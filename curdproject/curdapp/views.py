from django.shortcuts import render,redirect
from .models import StudentData
from django.http import HttpResponse

# Create your views here.
def students_form(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        cname=request.POST.get('cname')
        section=request.POST.get('section')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        odia=request.POST.get('odia')
        hindi=request.POST.get('hindi')
        eng=request.POST.get('eng')

        data=StudentData(first_name=fname,
                         last_name=lname,
                         class_name=cname,
                         section=section,
                         mob=mobile,
                         email=email,
                         odia=odia,
                         hindi=hindi,
                         eng=eng)
        data.save()
        students=StudentData.objects.all()


        return render(request,'students_data_inserting.html',{'students':students})
    else:
        students=StudentData.objects.all()
        return render(request,'students_data_inserting.html',{'students':students})


def update_data(request,id):
    student=StudentData.objects.get(id=id)
    if request.method=='POST':
        student.first_name=request.POST.get('fname')
        student.last_name=request.POST.get('lname')
        student.class_name=request.POST.get('cname')
        student.section=request.POST.get('section')
        student.mob=request.POST.get('mobile')
        student.email=request.POST.get('email')
        student.odia=request.POST.get('odia')
        student.hindi=request.POST.get('hindi')
        student.eng=request.POST.get('eng')
        # data=StudentData(first_name=fname,
        #                  last_name=lname,
        #                  class_name=cname,
        #                  section=section,
        #                  mob=mobile,
        #                  email=email,
        #                  odia=odia,
        #                  hindi=hindi,
        #                  eng=eng)
        student.save()
        return redirect('/')
        #return HttpResponse('<h2> Data Updated Successfully</h2>')
    else:

        return render(request,'update_data.html',{'student':student})




def delete_data(request,id):
    student=StudentData.objects.get(id=id)
    student.delete()
    return redirect('/')
    #return HttpResponse('<h2> Data Deleted Successfully</h2>')

