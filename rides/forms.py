from django import forms
from .models import *

class ReminderForm(forms.ModelForm):
	class Meta:
		model=Reminder
		exclude=('',)