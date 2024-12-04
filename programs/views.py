from django.shortcuts import render, redirect
from .models import ProgrammingLanguage


def language_list(request):
    languages = ProgrammingLanguage.objects.all()
    ctx = {'languages': languages}
    return render(request, 'programs/language_list.html', ctx)


def add_language(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ProgrammingLanguage.objects.create(title=title, description=description)
        return redirect('language_list')
    return render(request, 'programs/add_language.html')