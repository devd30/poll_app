from django import forms
from .models import Event,Ticket
import datetime


class EventForm(forms.Form):
    event_title = forms.CharField(max_length = 250)
    event_date  = forms.DateField(required = True)

    def save_event(self):
        event_title = self.cleaned_data['event_title']
        event_date  = self.cleaned_data['event_date']
        event = Event(event_title = event_title,event_date = event_date)
        event.save()
        return event

class TicketForm(forms.Form):
    ticket_title = forms.CharField(max_length = 250)
    start_date = forms.DateField(required = True)
    last_date = forms.DateField(required = True)
    
    def save_ticket(self,event_id):
        ticket_title = self.cleaned_data['ticket_title']
        start_date = self.cleaned_data['start_date']
        last_date = self.cleaned_data['last_date']
        ticket = Ticket(ticket_title = ticket_title,start_date = start_date,last_date = last_date,event_id_id = int(event_id))
        ticket.save()
        return ticket