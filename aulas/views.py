from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Aula, Agenda, Usuario
import datetime
import calendar
from django.utils.safestring import mark_safe
from .utils import EventCalendar, EventWeekCalendar
import locale

# Create your views here.
def index(request, extra_context=None):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return render(request, "aulas/user.html", {
            "message": "Anonimo"
        })
    username = request.user.id
    yesterday = datetime.date.today()-datetime.timedelta(days=1)
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

    aulas_usuario = Usuario.objects.filter(id=username)
    aulas = Agenda.objects.filter(data_aula__gte=yesterday).filter(aulas__username=username).order_by('data_aula')

    classes = Agenda.objects.all()
    filtro = Agenda.objects.filter(data_aula__gte=yesterday)
        
    after_day = request.GET.get('day__gte', None)
    extra_context = extra_context or {}
 
    if not after_day:
        d = datetime.date.today()
    else:
        try:
            split_after_day = after_day.split('-')
            d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
        except:
            d = datetime.date.today()
 
    previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
    previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
    previous_month = datetime.date(year=previous_month.year, month=previous_month.month, day=1)  # find first day of previous month
 
    last_day = calendar.monthrange(d.year, d.month)
    next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
    next_month = next_month + datetime.timedelta(days=1)  # forward a single day
    next_month = datetime.date(year=next_month.year, month=next_month.month,day=1)  # find first day of next month
 
    extra_context['previous_month'] = reverse('index') + '?day__gte=' + str(previous_month)
    extra_context['next_month'] = reverse('index') + '?day__gte=' + str(next_month)
 
    d = datetime.date.today()
    cal = EventCalendar()
    html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
    html_calendar = html_calendar.replace('<td ', '<td  width="200" height="200"')
    return render(request, "aulas/user.html", {
        "user"       : aulas_usuario,
        "aulas_user" : aulas,
        "classes"    : classes,
        "filtro"     : filtro,
        "calendar"   : mark_safe(html_calendar),
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

def agenda_view(request, extra_context=None):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return render(request, "aulas/user.html", {
            "message": "Anonimo"
        })
    username = request.user.id
    yesterday = datetime.date.today()-datetime.timedelta(days=1)
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

    aulas_usuario = Usuario.objects.filter(id=username)
    aulas = Agenda.objects.filter(data_aula__gte=yesterday).filter(aulas__username=username).order_by('data_aula')

    classes = Agenda.objects.all()
    filtro = Agenda.objects.exclude(aulas__username=username).filter(data_aula__gte=yesterday)
        
    after_day = request.GET.get('day__gte', None)
    extra_context = extra_context or {}
 
    if not after_day:
        d = datetime.date.today()
    else:
        try:
            split_after_day = after_day.split('-')
            d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
        except:
            d = datetime.date.today()
 
    previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
    previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
    previous_month = datetime.date(year=previous_month.year, month=previous_month.month, day=1)  # find first day of previous month
 
    last_day = calendar.monthrange(d.year, d.month)
    next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
    next_month = next_month + datetime.timedelta(days=1)  # forward a single day
    next_month = datetime.date(year=next_month.year, month=next_month.month,day=1)  # find first day of next month
 
    extra_context['previous_month'] = reverse('index') + '?day__gte=' + str(previous_month)
    extra_context['next_month'] = reverse('index') + '?day__gte=' + str(next_month)
 
    d = datetime.date.today()
    cal = EventCalendar()
    html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
    html_calendar = html_calendar.replace('<td ', '<td  width="200" height="200"')
    return render(request, "aulas/agenda.html", {
        "user"       : aulas_usuario,
        "aulas_user" : aulas,
        "classes"    : classes,
        "filtro"     : filtro,
        "calendar"   : mark_safe(html_calendar),
    } )

def calendar_view(request, extra_context=None):
    yesterday = datetime.date.today()-datetime.timedelta(days=1)
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
        
    after_day = request.GET.get('day__gte', None)
    extra_context = extra_context or {}
 
    if not after_day:
        d = datetime.date.today()
    else:
        try:
            split_after_day = after_day.split('-')
            d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
        except:
            d = datetime.date.today()

    d = datetime.date.today()
    cal = EventCalendar()
    html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
    html_calendar = html_calendar.replace('<td ', '<td  width="200" height="200"')
    return render(request, "aulas/calendar.html", {
        "calendar"   : mark_safe(html_calendar),
    } )

def marcar_view(request):
    
    username = request.user.id
    if request.method == "POST":
        print(request.POST)
        items = request.POST.getlist("item")
        print(items)
        for item in items:
            print(item)
            # implement logic to add the item id (aula) to the user
            agenda = Agenda.objects.get(id=item)
            user = Usuario.objects.get(username=username)
            user.agendas.add(agenda)
            # implement logic to update the item id (aula) increase numero_alunos field
            numero = agenda.numero_alunos
            Agenda.objects.filter(id=item).update(numero_alunos=numero+1)
            alerta = "AULA MARCADA!!"
    
    yesterday = datetime.date.today()-datetime.timedelta(days=1)
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    filtro = Agenda.objects.exclude(aulas__username=username).filter(data_aula__gte=yesterday)
    return render(request, "aulas/agenda.html", {
        "filtro"     : filtro,
        "alerta" : alerta,
    } )    