from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):

    status = forms.CharField(widget=forms.HiddenInput, initial='Pending')

    class Meta:
        model = Ticket
        fields = ['name', 'last_name', 'department_name', 'request_type', 'description', 'attachment']
        exclude = ['status']
    attachment = forms.FileField(required=False)