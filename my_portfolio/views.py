from django.shortcuts import render, redirect
from .models import ContactMessage, Project
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import DetailView

def home(request):
  projects = Project.objects.all()[:3]
  return render(request, 'home.html',{'projects':projects})


def about(request):
    # Context data to pass to the template
    context = {
        'profile_image_url': '/path/to/profile/image.jpg',  # Update with your image path
        'bio': "I am a Computer Science graduate and an enthusiastic Django developer with a strong foundation in full-stack web development.",
        'categorized_skills': {
            'Programming Languages': ['Python', 'JavaScript'],
            'Web Technologies': ['HTML5', 'CSS3', 'React.js', 'Node.js'],
            'Databases': ['MySQL', 'MongoDB'],
            'Tools & Platforms': ['Git', 'Docker', 'AWS'],
            'Soft Skills': ['Communication', 'Teamwork', 'Problem-Solving']
        },
        'github_url': 'https://github.com/AbdulKareem',
        'linkedin_url': 'https://www.linkedin.com/in/abdu1kareem',
        'twitter_url': 'https://twitter.com/YourProfile'
    }
    return render(request, 'about.html', context)



def projects(request):
  project_list = Project.objects.all().order_by('-created_at')
  return render(request,'projects.html',{'project_list':project_list})


class ProjectDetailView(DetailView):
  model = Project
  template_name = 'project_detail.html'  # Specify your template name here
  context_object_name = 'project'


# Contact Page View with Database Storage
def contact(request):
  if request.method == 'POST':
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    message = request.POST.get('message', '').strip()

    if not name or not email or not message:
      messages.error(request, 'All fields are required!')
    else:
      try:
        # Save message in the database
        ContactMessage.objects.create(name=name, email=email, message=message)
        
        # Send email notification
        send_mail(
          f'Message from {name}',
          message,
          settings.DEFAULT_FROM_EMAIL,
          ['abdulkareemyuseph@gmail.com'],
          fail_silently=False,
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('message_success')
      except Exception:
        messages.error(request, 'Failed to send message. Please try again later.')
  return render(request, 'contact.html')


def message_success(request):
    return render(request, 'message_success.html')

def contact_messages(request):
  messages_list = ContactMessage.objects.all().order_by('-created_at')
  return render(request, 'contact_messages.html', {'messages_list': messages_list})