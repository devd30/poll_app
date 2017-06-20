from django.conf.urls import url

from . import views

app_name ='Events'

urlpatterns = [
        url(r'^$', views.events, name='events'),
        url(r'^addevent/$',views.addevent,name='addevent'),
        url(r'^events/$',views.events,name='event'),
        url(r'^fetchEvents/$',views.fetchEvents,name='fetchEvents'),
        url(r'^fetch_tickets/(?P<event_id>[0-9]+)$',views.fetch_event_tickets,name='fetch_tickets'),
        url(r'^add_ticket/(?P<event_id>[0-9]+)$',views.addTicket,name='add_tickets'),
        url(r'^tickets/(?P<event_id>[0-9]+)$',views.tickets,name='tickets'),
        ]


