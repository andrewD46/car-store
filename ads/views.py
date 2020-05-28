from django.shortcuts import render
from ads.forms import AdForm


def create(request):
    if request.method == 'GET':
        form = AdForm()
        return render(request, 'create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        pass
