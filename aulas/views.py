from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Aula, Agenda, Usuario
import datetime

# Create your views here.
def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return render(request, "aulas/user.html", {
            "message": "Anonimo"
        })
    username = request.user.id
    print(f"username id: {username}"  )
    print(f"usuarios : {Usuario.objects.all()}"  )
    aulas_usuario = Usuario.objects.filter(id=username)
    print(aulas_usuario)
    aulas = Agenda.objects.filter(aulas__username=username)
    print(aulas)
    classes = Agenda.objects.all()
    print(classes)
    current_date = datetime.date.today()-datetime.timedelta(days=1)
    print(f"Current date {current_date}")
    filtro = Agenda.objects.filter(data_aula__gte=current_date)
    print(filtro)
    return render(request, "aulas/user.html", {
        "user"       : aulas_usuario,
        "aulas_user" : aulas,
        "classes"    : classes,
        "filtro"     : filtro
    } )

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "aulas/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "aulas/login.html")

def logout_view(request):
    logout(request)
    return render(request, "aulas/login.html", {
                "message": "Logged Out"
            })