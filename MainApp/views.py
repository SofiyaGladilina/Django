from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Гладилина С.А.</i>
    """
    return HttpResponse(text)



def about(request):
    user = """
    Имя: София <br>
    Отчество: Александровна<br>
    Фамилия: Гладилина<br>
    телефон: 8-923-600-01-02<br>
    email: sofiya.gladilina@yandex.ru"""
    return HttpResponse(user)

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124}
]




def get_item(request, item_id):
    for item in items:
        if item['id'] == item_id:
            result = f"""
            <h2>Имя: {item["name"]}</h2>
            <p> Количество: {item["quantity"]}
            <p><a href="items">Назад к списку товаров</a>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f"Item with id={item_id} not found")


def get_items(request):
    result = "<h1>Список товаров<h1><ol>"
    for item in items:
        result += f""" <li><a href="/item/{item['id']}">{item['name']}</li> """
    result += "</ol>"
    return HttpResponse(result)





        


   
    




