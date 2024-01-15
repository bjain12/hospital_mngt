from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient, Appointment

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    d=0
    p=0
    ap=0
    for i in doctors:
        d +=1
    for i in patient:
        p+=1
    for i in appointment:
        ap +=1
    d1 = {'d': d, 'p': p, 'ap': ap}
    return render(request, 'index.html', d1)

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username =u, password = p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc' : doc}
    return render(request, 'view_doctor.html', d)

def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id = pid)
    doctor.delete()
    return redirect('view_doctor')

def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['speciality']
        try:
            Doctor.objects.create(Name = n, mobile = m, speciality = sp)
            error='no'
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_doctor.html', d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()
    d = {'doc' : doc}
    return render(request, 'view_patient.html', d)


def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id = pid)
    patient.delete()
    return redirect('view_patient')

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['name']
        gd = request.POST['gender']
        m = request.POST['mobile']
        add = request.POST['address']
        try:
            Patient.objects.create(name = n, gender =gd, mobile = m, address = add)
            error='no'
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)



def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.all()
    a = {'app' : app}
    return render(request, 'view_appointment.html', a)


def Delete_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id = pid)
    appointment.delete()
    return redirect('view_appointment')


def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == "POST":
        dn = request.POST['doctor']
        pn = request.POST['patient']
        da = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(Name = dn).first()
        patient = Patient.objects.filter(name = pn).first()

        if doctor is not None and patient is not None:
            try:
                Appointment.objects.create(doctor=doctor, patient=patient, date=da, time=t)
                error='no'
            except Exception as e:
                error = "yes"
                print(e)
        else:
            error = "invalid_doctor_or_patient"
    d = {'doctor1': doctor1, 'patient1': patient1, 'error': error}
    return render(request, 'add_appointment.html', d)