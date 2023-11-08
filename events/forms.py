from django import forms
from .models import Event


class EventsForm(forms.Form):
    model = Event
    fields = ["event_name", "start_time", "end_time", "capacity"]


class EventFilterForm(forms.Form):
    start_time = forms.DateTimeField(required=False)
    end_time = forms.DateTimeField(required=False)
    min_capacity = forms.IntegerField(min_value=0, required=False)
    max_capacity = forms.IntegerField(min_value=0, required=False)
