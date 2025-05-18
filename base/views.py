from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from django.core.mail import send_mail
from base.form import ContactForm
from django.conf import settings
from django.contrib import messages
# Create your views here.

def home(request):

    return render(request,'home.html')

def project(request):
    project_details=[
         {
            'id': 1,
            'title':'Task Management System',
            'path':'images/projectimg/task-01.png',
            'desc': '''A Django Task Management System using CRUD operations allows users to Create, Read, Update, and Delete tasks.It provides interfaces for users to add new tasks with details like title, description, and deadline.Users can view task lists and individual task details dynamically from the database.Editing task information and updating status is handled through Django forms.Tasks can also be deleted securely, ensuring proper management and cleanup of data.'''
        },
        {   'id': 2,
            'title':'Shopsphere',
            'path':'images/projectimg/pro-03.png',
            'desc': '''A Django e-commerce project is a web application for buying and selling products online.It uses Django's powerful backend to manage users, products, orders, and payments securely.The admin panel allows easy management of inventory and order tracking.User authentication and shopping cart features enhance the customer experience.It can integrate with payment gateways and be customized for various business needs.'''
        },
    ]
    return render(request,'project.html',{"project_details":project_details})

def about(request):

    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            data=form.save()
            subject = data.email_subject
            message= f"""{data.full_name}{data.email} {data.mobile_no} {data.message_box}"""
            send_mail(subject,message,settings.DEFAULT_FROM_EMAIL,['kingrahan32@gmail.com'])
            messages.success(request, "Message sent successfully!")
            return redirect('contact')  
            
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})

# views.py

def project_detail(request, project_id):
    # Ideally, use a database model; for now, hardcoded example:
    projects = {
        1: {
            'title': 'Task Management System',
            'images': ['images/projectimg/task-01.png', 'images/projectimg/task-02.png' ,'images/projectimg/task-03.png']
        },
        2: {
            'title': 'Shopsphere',
            'images': ['images/projectimg/pro-01.png', 'images/projectimg/pro-02.png','images/projectimg/pro-03.png','images/projectimg/pro-04.png','images/projectimg/pro-05.png','images/projectimg/pro-06.png','images/projectimg/pro-07.png','images/projectimg/pro-08.png']
        }
    }

    project = projects.get(project_id)
    if not project:
        return HttpResponseNotFound("Project not found")

    return render(request, 'project_detail.html', {'project': project})
