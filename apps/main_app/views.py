from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import Admin, Mission
# Create your views here.
def index(request):
    context = {
        'missions':Mission.objects.all().order_by('-created_at'),
        'admin':Admin.objects.get(id = request.session['admin_id']),
    }
    return render(request, 'main_app/index.html', context)

def log(request):
    return render(request, 'main_app/log.html')

def rules(request):
    return render(request, 'main_app/rulebook.html')

def admin(request):
    return render(request, 'main_app/admin.html')

def submit(request):
    return

def success(request):
    return

def reject(request):
    return

def login(request):

    return render(request, 'main_app/login.html')

def admin_index(request):
    return render (request, 'main_app/loginadmin.html')

def admin_login(request):
   response = Admin.objects.login(request.POST)
   print response
   if not response['status']:
       for error in response['errors']:
           messages.error(request,error)
       return redirect('mission:admin_login')
   else:
       admin = Admin.objects.get(username = request.POST['username'])
       request.session['admin_id'] = admin.id
       return redirect('mission:admin')

def create_team(request):
    return


def submit_mission(request):
    return


def create_mission(request):
    admin=Admin.objects.get(id=request.session['id'])
    Mission.objects.create(name=request.POST['mission_name'], description=request.POST['mission_description'],rating=request.POST['mission_difficulty'], admin=admin )
    return redirect('mission:index')

def admin_registration(request):
    if not request.POST.get('password') == request.POST.get('confirm_password'):
        messages.error(request, 'Password did not match.')
    else:
        # password=bcrypt.hashpw(request.POST.get('password', '').encode('utf-8'),bcrypt.gensalt())
        password=bcrypt.hashpw(request.POST['password'].encode('utf-8'),bcrypt.gensalt())
        admin=Admin.objects.create(username=request.POST['username'], password=password, )#created admin, storing all ex: Amy's informtion in admin.
        request.session['admin_id']=admin.id #taking only the id form Admin.
    return redirect ('mission:admin')
