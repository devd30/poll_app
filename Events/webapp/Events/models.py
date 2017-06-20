from django.db import models
import datetime

# Create your models here.
class Event(models.Model):
    class Meta:
        db_table = "Events"

    event_title = models.CharField(max_length = 250)
    event_date = models.DateTimeField('event date')

class Ticket(models.Model):
    class Meta:
        db_table = "Ticket"

    ticket_title = models.CharField(max_length=250)
    start_date = models.DateTimeField('start date for ticket')
    last_date = models.DateTimeField('last date for ticket')
    event_id = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="ticket")