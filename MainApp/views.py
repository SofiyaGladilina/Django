from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse


user = """
    Имя: Иван <br>
    Отчество: Петрович<br>
    Фамилия: Иванов<br>
    телефон: 8-923-600-01-02<br>
    email: vasya@mail.ru"""
def about(request):
    return HttpResponse(user)
    




