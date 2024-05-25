from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    context = """
    "name" = "Петров Иван Николаевич"
    "email" = "my@email.ru"
"""
    
    return render(request, 'index.html', context)




