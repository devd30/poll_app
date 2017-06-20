from django.shortcuts import get_object_or_404, render
from .models import Event ,Ticket
from .forms import EventForm , TicketForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, \
    require_GET, require_POST
from django.http import HttpResponse, JsonResponse, Http404
from datetime import datetime

# Create your views here.
@csrf_exempt
def events(request):
    return render(request , 'Events/eventspage.html')

@csrf_exempt
def addevent(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        event_date = request.POST['event_date']
        event_date = datetime.strptime(event_date, '%Y-%m-%d').date()
        if event_date < datetime.now().date():
            return JsonResponse({"error":"Invalid Event Date"},status=411)
        if form.is_valid():
            event = form.save_event()
        data = {}
        data['event_title'] = event.event_title
        data['event_date'] = event.event_date
        data['event_id'] = event.id
        return JsonResponse(data=data,safe=False)


@require_GET
def fetchEvents(requests):
    data =[]
    event_objects = Event.objects.all()
    for event_object in event_objects:
        data.append({"event_id":event_object.id,"event_title":event_object.event_title,"event_date":event_object.event_date})
    return JsonResponse(data = data,safe=False) 

@require_GET
def fetch_event_tickets(request,event_id):
    data = []
    event = Event.objects.get(pk=event_id)
    tickets = event.ticket.all()
    for ticket in tickets:
        data.append({"event_title":event.event_title,"ticket_id":ticket.id,"ticket_title":ticket.ticket_title,"start_date":ticket.start_date,"last_date":ticket.last_date})
    return JsonResponse(data = data , safe = False)

@csrf_exempt
def addTicket(request,event_id):
    if request.method == "POST":
        form = TicketForm(request.POST)
        event = Event.objects.get(pk=event_id)
        event_date = event.event_date.date()
        start_date = request.POST['start_date']
        start_date = datetime.strptime(start_date,'%Y-%m-%d').date()
        last_date = request.POST['last_date']
        last_date = datetime.strptime(last_date,'%Y-%m-%d').date()
        if (start_date > event_date) or (start_date < datetime.now().date()):
            return JsonResponse({"message":"Invalid Start Date"},status=411)
        if (last_date <= start_date) or (last_date > event_date):
            return JsonResponse({"message":"Invalid Last Date"},status=411)
        if form.is_valid():
            ticket = form.save_ticket(event_id)
        data = {}
        data['event_title'] = event.event_title
        data['ticket_title'] = ticket.ticket_title
        data['start_date'] = ticket.start_date
        data['last_date'] = ticket.last_date
        data['ticket_id'] = ticket.id
        return JsonResponse(data=data , safe = False)

@csrf_exempt
def tickets(request,event_id):
    return render(request,'Events/ticketspage.html',{"event_id":event_id})
