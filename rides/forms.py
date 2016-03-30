from django import forms
from .models import *


class RemainderForm(forms.ModelForm):
	class Meta:
		model=Remiander
		exclude=('',)