from calendar import HTMLCalendar
from datetime import datetime as dtime, date, time
import datetime
from .models import Agenda
from django.http import HttpResponseRedirect
 
class EventCalendar(HTMLCalendar):
    def __init__(self, agendas=None):
        super(EventCalendar, self).__init__()
        self.agendas = agendas
 
    def formatday(self, day, weekday, agendas):
        """
        Return a day as a table cell.
        """
        events_from_day = agendas.filter(data_aula__day=day)
        events_html = "<ul>"
        for event in events_from_day:
            events_html += f"<button>{event.hora_inicio}:{event.hora_fim} - {event.aula.aula} </button><br>"
        events_html += "</ul>"
 
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)
 
    def formatweek(self, theweek, events):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s
 
    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
 
        agendas = Agenda.objects.filter(data_aula__month=themonth)
 
        v = []
        a = v.append
        a('<table border="1" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, agendas))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

class EventWeekCalendar(HTMLCalendar):
    def __init__(self, agendas=None):
        super(EventWeekCalendar, self).__init__()
        self.agendas = agendas
 
    def formatday(self, day, weekday, agendas):
        """
        Return a day as a table cell.
        """
        events_from_day = agendas.filter(data_aula__day=day)
        events_html = "<ul>"
        for event in events_from_day:
            events_html += str(event.hora_inicio) + " " + str(event.hora_fim) + " " + str(event.aula.aula) + "<br>"
        events_html += "</ul>"
 
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)
 
    def formatweek(self, theweek, events):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s
 
    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
 
        agendas = Agenda.objects.filter(data_aula__month=themonth)

        d = datetime.date.today() 
        v = []
        a = v.append
        a('<table border="1" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            if (d.day in week):
                a(self.formatweek(week, agendas))
                a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)