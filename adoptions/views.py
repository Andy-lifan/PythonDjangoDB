from django.shortcuts import render
from django.http import Http404, HttpResponse 
from .models import Pet, Vaccine, Student 
import csv
from .forms import StudentForm 
from reportlab.pdfgen import canvas  

  
def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Andy.")  
    p.showPage()  
    p.save()  
    return response  

def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('andyiot', 'www.andyiot.com')  
    return response  

def getcookie(request):  
    tutorial  = request.COOKIES['andyiot']  
    return HttpResponse("iot tutorials @: "+  tutorial);  

def setsession(request):  
    request.session['sname'] = 'Andy'  
    request.session['semail'] = 'andyzhang@gmail.com'  
    return HttpResponse("session is set") 

def getsession(request):  
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    return HttpResponse(studentname+" "+studentemail)
  
def index(request):  
    student = StudentForm()  
    return render(request,"index.html",{'form':student})  

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets':pets,})
    #return HttpResponse('<p>home view</p>')

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
         raise Http404('pet not found')
    return render(request, 'pet_details.html', {'pet': pet, })
    #return HttpResponse(f'<p>pet_detail view with id {pet_id}</p>')

def student(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students':students,})

def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    pets = Pet.objects.all()  
    writer = csv.writer(response)  
    for pet in pets:  
        writer.writerow([pet.name,pet.submitter,pet.species, pet.breed, pet.description])  
    return response  