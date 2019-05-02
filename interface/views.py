from django.shortcuts import render
from django.shortcuts import redirect, render_to_response
from .forms import FlexibleForm


def homepage(request):

    if request.method == 'POST':
        form = FlexibleForm(request.POST)
        if form.is_valid():
            print(form)

    form = FlexibleForm()
    return render(request, 'form.html', {'form': form})
