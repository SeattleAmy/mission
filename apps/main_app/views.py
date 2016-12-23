from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import Admin, Mission
# Create your views here.
def index(request):
    context = {
        'missions':Mission.objects.filter(status = "incomplete").order_by('-created_at')| Mission.objects.filter(status = "Try again!"),
        'admin':Admin.objects.get(id = request.session['admin_id']),
    }
    return render(request, 'main_app/index.html', context)

def log(request):
    context ={
        'complete_missions':Mission.objects.filter(status = 'complete')
    }
    return render(request, 'main_app/log.html', context)

def rules(request):
    return render(request, 'main_app/rulebook.html')

def admin(request):
    context = {
        'pending_missions':Mission.objects.filter(status = "pending")
    }
    return render(request, 'main_app/admin.html', context)

def submit(request):
    return

def success(request, id):
    Mission.objects.filter(id = id).update(status = "complete")
    mission = Mission.objects.get(id = id)
    if not "total_score" in request.session:
        request.session['total_score'] = mission.rating
    else:
        request.session['total_score'] += mission.rating
    print "*" * 50
    print mission.rating
    return redirect('mission:admin')

def reject(request, id):
    Mission.objects.filter(id = id).update(status = "Try again!")
    return redirect('mission:admin')

def login(request):

    return render(request, 'main_app/login.html')

def reset(request):
    request.session['total_score'] = 0
    return redirect('mission:index')

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


def submit_mission(request, id):
    Mission.objects.filter(id = id).update(status = "pending")
    ###WORKINGO NTHIS  SEND MISSION TO PENDING LOG. CHANGE CONTEXT FILTERS
    return redirect('mission:index')


def create_mission(request):
    admin=Admin.objects.get(id=request.session['admin_id'])
    Mission.objects.create(name=request.POST['mission_name'], description=request.POST['mission_description'],rating=request.POST['mission_difficulty'], admin=admin )
    return redirect('mission:admin')

def admin_registration(request):
    if not request.POST.get('password') == request.POST.get('confirm_password'):
        messages.error(request, 'Password did not match.')
    else:
        # password=bcrypt.hashpw(request.POST.get('password', '').encode('utf-8'),bcrypt.gensalt())
        password=bcrypt.hashpw(request.POST['password'].encode('utf-8'),bcrypt.gensalt())
        admin=Admin.objects.create(username=request.POST['username'], password=password, )#created admin, storing all ex: Amy's informtion in admin.
        request.session['admin_id']=admin.id #taking only the id form Admin.
    return redirect ('mission:admin')
