from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from base.models import EmailSettings
from django.shortcuts import render, redirect

def edit_email_settings(request):
    if request.method == 'POST':
        sender_email = request.POST.get('sender_email')
        password = request.POST.get('password')
        print("run")
        print(sender_email,password)
        # Assuming there is only one EmailSettings instance in the database
        settings_instance = EmailSettings.objects.first()
        print(settings_instance)
        if settings_instance:
            settings_instance.sender_email = sender_email
            settings_instance.password = password
            settings_instance.save()
            print("data updated")
            # You can return a JSON response to indicate success
            return redirect("show_email_settings")
        else:
            obj = EmailSettings(sender_email=sender_email,password=password)
            obj.save()
            return redirect("show_email_settings")
    else:
        settings_instance = EmailSettings.objects.first()
        return render(request, 'mail/edit_email_settings.html', {'settings': settings_instance})

def show_email_settings(request):
    settings_instance = EmailSettings.objects.first()
    return render(request, 'mail/show_email_settings.html', {'settings': settings_instance})
