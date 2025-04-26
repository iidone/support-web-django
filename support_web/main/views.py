from django.shortcuts import render, redirect
from django.views import View
from django.contrib.admin.views.decorators import staff_member_required
from .models import Issues
from .models import Moderators
from .models import Problems
from .models import Directions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage 
from django.utils.timezone import now 
import os
import socket
import getpass

def send_issue_to_moderator(issue_id, moderator_name, issue):
    moderator = User.objects.get(first_name=moderator_name)
    moderator_mail = moderator.email


    email = EmailMessage(
        f'Новая заявка от пользователя {issue.user_name} - {issue.issue}',
        issue.issue_description,
        'your_mail@yandex.ru',
        [moderator_mail],
    )

    email.attach_file(issue.image.path)
    email.send()

def login(request):
    issues = Issues.objects.all()
    moderators = Moderators.objects.all()
    
    if request.method == "POST":
        username = request.POST.get('username')
        username_global = username
        print(username_global)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    
        if user is not None and user.is_staff: 
            auth_login(request, user)
            messages.success(request, "")
            return redirect(moders)
        else:
            messages.error(request, "Неверные учетные данные или у вас недостаточно прав. Пожалуйста, попробуйте снова.")

    return render(request, 'main/login.html', {'issues': issues, 'moderators': moderators})

def loginToControl(request):
    issues = Issues.objects.all()
    moderators = Moderators.objects.all()
    
    if request.method == "POST":
        username = request.POST.get('username')
        username_global = username
        print(username_global)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    
        if user is not None and user.is_staff: 
            auth_login(request, user)
            messages.success(request, "")
            return redirect(control)
        else:
            messages.error(request, "Неверные учетные данные или у вас недостаточно прав. Пожалуйста, попробуйте снова.")

    return render(request, 'main/login.html', {'issues': issues, 'moderators': moderators})

@csrf_exempt
@login_required
@staff_member_required
def control(request):
    issues = Issues.objects.filter(status = "Не рассмотрена")
    moderators = User.objects.filter(is_staff = True)
    success2 = False
    issue_id = None
    moderator_name = None
    moderator_mail = None

    if request.method == "POST":
        issue_id = request.POST.get('issue')
        moderator_name = request.POST.get('moderator')

        if issue_id:
            try:
                issue = Issues.objects.get(id=issue_id)
                issue.status = "Отправлена модератору"
                direction = Directions.objects.create(
                    issue=issue.issue,
                    moderator=moderator_name,
                )
                issue.save()
                direction.save()


                send_issue_to_moderator(issue_id, moderator_name, issue)

                success2 = True 
            except Issues.DoesNotExist:
                messages.error(request, "Заявка не найдена.")
        else:
            messages.error(request, "Пожалуйста, выберите заявку.")

    return render(request, 'main/control.html', {
        'issues': issues,
        'moderators': moderators,
        'success': success2,
        'issue': issue_id,
        'moderator': moderator_name
    })
    
@csrf_exempt
def index(request):
    problems = Problems.objects.filter(parent = None)  
    

    if request.method == "POST":
        print("Форма отправлена")
        problem = request.POST.get('problem')
        subproblem = request.POST.get('subproblem')
        full_problem = problem +  " -- " + subproblem
        description = request.POST.get('description')
        phone = request.POST.get('phone')
        image = request.FILES.get('file')
        user_name = getpass.getuser()
        pc_name = socket.gethostname()

        if not problem or not description or not image:
            messages.error(request, "Пожалуйста, заполните все поля.")
            return render(request, 'main/index.html', {'user': request.user})
        
        issue = Issues.objects.create(
            user_name=user_name,
            pc_name=pc_name,
            issue=full_problem,
            issue_description=description,
            phone=phone,
            image=image,
            status = "Не рассмотрена"
        )
        issue.save()
        print("Заявка отправлена")
        messages.success(request, "Заявка успешно отправлена!")

    user = request.user
    return render(request, 'main/index.html', {'user': user, 'problems': problems})

@csrf_exempt
@login_required
@staff_member_required
def moders(request):
    moderators = Moderators.objects.all()
    issues = Issues.objects.filter(status = "Не рассмотрена")
    issue_id = None
    
    if request.method == "POST":
        print(request.POST)
        issue_id = request.POST.get('issue')
        if not issue_id or not issue_id.isdigit():
            print(request, "Неверный идентификатор заявки.")
            return redirect('moders')
        moderator_name = request.user.first_name
        print(issue_id)
        
        issue = Issues.objects.get(id = issue_id)
        issue.status = "Отправлена модератору"
        direction = Directions.objects.create(
            issue=issue.issue,
            moderator=moderator_name,
        )
        issue.save()
        direction.save()
        
            
    return render(request, 'main/mod_tables.html', {'user': request.user , 'issues' : issues})


@csrf_exempt
@login_required
@staff_member_required
def moder_home(request):
    user = request.user
    moderator_name = user.first_name
    directions = Directions.objects.filter(moderator = moderator_name)
    issues = Issues.objects.filter(issue__in = [direction.issue for direction in directions], status = "Отправлена модератору")
    
    if request.method == "POST":
        print(request.POST)
        issue_id = request.POST.get('issue')
        post_moderator_name = f"{user.first_name} {user.last_name}"
        moderator = Moderators.objects.get(full_name = post_moderator_name)
        issue = Issues.objects.get(id = issue_id)
        issue.closing_time = now()
        issue.status = "Закрыта"
        moderator.month_tickets += 1
        
        
        moderator.save()
        issue.save()
    return render(request, 'main/moderator_home.html', {'issues': issues})