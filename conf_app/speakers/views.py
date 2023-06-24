from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def speaker_list(request):
    return render(request, 'speaker_list.html')

def speaker_create(request):
    return render(request, 'speaker_create.html')

def speaker_detail(request, pk):
    return render(request, 'speaker_detail.html')

def speaker_update(request, pk):
    return render(request, 'speaker_update.html')

def speaker_delete(request, pk):
    return render(request, 'speaker_delete.html')
