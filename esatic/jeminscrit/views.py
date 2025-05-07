from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InscriptionForm
from .models import Candidat
from django.template.loader import render_to_string
from django.conf import settings

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            candidat = form.save()
            return redirect('confirmation', candidat_id=candidat.id)
    else:
        form = InscriptionForm()
    
    context = {
        'form': form,
        'title': 'Inscription aux concours ESATIC'
    }
    return render(request, 'inscriptions.html', context)

def confirmation(request, candidat_id):
    candidat = Candidat.objects.get(id=candidat_id)
    context = {
        'candidat': candidat,
        'title': 'Confirmation inscription'
    }
    return render(request, 'confirmation.html', context)

def imprimer_confirmation(request, candidat_id):
    candidat = Candidat.objects.get(id=candidat_id)
    context = {'candidat': candidat}
    html = render_to_string('impression.html', context)
    return HttpResponse(html, content_type='text/html')