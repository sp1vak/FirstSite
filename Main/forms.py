from .models import Notes
from django.forms import ModelForm, TextInput, Textarea


class NoteForm(ModelForm):
	class Meta:
		model = Notes
		fields = ['title', 'note']
		widgets = {
			"title": TextInput(attrs = {
			'class': 'form-bg-dark alert show,',
			'placeholder': 'Enter name'
			}),
			"note": Textarea(attrs = {
			'class': 'form-bg-dark alert show,',
			'placeholder': 'Enter description'
		})
	}
