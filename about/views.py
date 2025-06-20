from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import CollaborateForm  #  Import the form


# Create your views here.



def about_me(request):
    """
    Renders the About page and processes the collaboration form
    """
    about = About.objects.all().order_by('-updated_on').first()
   
    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(request, "Thank you! We'll be in touch soon.")  # Success message
            return redirect("about")  # Prevents resubmission on refresh
    else:
        collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )