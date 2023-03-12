from django.http import HttpResponse
from django.shortcuts import render
from .models import*

menu=["about", "Log In" ,"Categories"]
def index(request):
    posts=Product.objects.all()
    cats =Category.objects.all()

    context ={
        'cats': cats,
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,

    }
    return render(request, 'main/index.html',context=context)

def about(request):
    return render(request, 'main/about.html',{'menu':menu,'title':'about'})

def categories(request, catid):
    print(request.GET)
    return HttpResponse(f"<h1>Категория</h1><p>{catid}</p>")

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_category(request, cat_id):
    return HttpResponse(f"Отображение категории с id = {cat_id}")








def handler400(request, exception):
    return render(request, "400.html", status=400)


def handler403(request, exception):
    return(render(request, "403.html", status=403))


def handler404(request, exception):
    return(render(request, "404.html", status=404))


def handler500(request):
    return(render(request, "500.html", status=500))

