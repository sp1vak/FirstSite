from django.shortcuts import render, redirect
from .models import Notes
from .forms import NoteForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(requests):
	notes = Notes.objects.all()
	return render(requests, 'Main/index.html', {'notes': notes})

def create(requests):
	error = ''
	if requests.method == 'POST':
		form = NoteForm(requests.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			error = 'Form isn`t valid'

	form = NoteForm()
	context = {
		'form': form,
		'error': error
	}
	return render(requests, 'main/create.html', context)

def edit(requests, id):
	notes = Notes.objects.get(id=id)
	if requests.method == 'POST':
		notes.title = requests.POST.get('title')
		notes.note = requests.POST.get('note')
		notes.save()
		return HttpResponseRedirect('/')
	else:
		return render(requests, 'main/create.html', {'notes': notes})


def delete(requests, id):
	note = Notes.objects.get(id=id)
	note.delete()
	return HttpResponseRedirect("/")

"""
def delete(requests):
	error = ''	
	if requests.method == 'POST':
		form = DeleteNoteForm(requests.POST)
		if form.is_valid():
			form.delete()
			return redirect('/')
		else:
			error = 'Form isn`t valid'

	form = DeleteNoteForm()
	context = {
		'form': form,
		'error': error
	}
	return render(requests, 'main/delete.html', context)
"""