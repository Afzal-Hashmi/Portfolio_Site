from django.shortcuts import render,redirect

from .models import Hero,Education,Skill,contact,skill_list

# Create your views here.

def index(request):

    hero = Hero.objects.first()
    education = Education.objects.all()
    skill = Skill.objects.first()
    list = skill_list.objects.all()

    return render(request, 'index.html',{
        'Hero': hero,
        'Education': education,
        'kill': skill,
        'list_skills': list
    })

def contactme(request):
    if request.method == 'POST':
        name = request.POST['name'],
        email = request.POST['email'],
        phone = request.POST['phone']
        contact.objects.create(name=name,email=email,phone=phone)
        return redirect('index')
    else:
        print ('something went wrong request.method is not POST')
        return redirect('index')