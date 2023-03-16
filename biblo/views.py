from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import*

menu=["about", "Log In" ,"Categories"]

# class ProductHome(ListView):
#     model = Product
#     template_name ='main.index.html'
#     context_object_name = 'posts'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context =super().get_context_data(**kwargs)
#         context['menu']=menu
#         context['title']='Главная страница'
#         context['cat_selected']='0'
#         return context
#
#     def get_queryset(self):
#       return  Product.objects.filter(is_published=True)

# class AddPage(CreateView):
#     form_class = AddPostForm
#     template_name = 'main/addpage.html'
#     success = reverse_lazy('home')
#
#     def get_context_data(self,*, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu']=menu
#         context['title']='Добавление статьи'
#         return context
def index(request):
    posts=Product.objects.all()

    context ={
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
    if request.method =='POST':
        form=AddPostForm(request.POST ,request.FILES)
        if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form=AddPostForm()
    return render( request, 'main/addpage.html',{'form':form ,'menu': menu , 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request, post_slug):
    post = get_object_or_404(Product, pk=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': 'post.title ',
        'cat_selected': post.cat_id,
    }
    return render(request, 'main/post.html', context=context)

# class ShowPost(DetailView):
#     model= Product
#     template_name = 'main/index.html'
#     slug_url_kwarg = 'post_slug'
#     context_object_name = 'post'
#     def get_context_data(self, *,object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = context['post']
#
#         return context



# class ProductCategory(ListView):
#     model= Product
#     template_name = 'main/index.html'
#     context_object_name = 'posts'
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = 'Категория -' +str(context['posts'][0].cat)
#         context['cat_selected'] = context['posts'][0].cat_id
#         return context
#
#     def get_queryset(self):
#         return Product.objects.filter(cat__slug=self.kwargs['car_slug'], is_published=True)

def show_category(request, cat_id):
    posts = Product.objects.filter(cat_id = cat_id)
    context = {

        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам ',
        'cat_selected': cat_id,

    }
    return render(request, 'main/index.html', context=context)









def handler400(request, exception):
    return render(request, "400.html", status=400)


def handler403(request, exception):
    return(render(request, "403.html", status=403))


def handler404(request, exception):
    return(render(request, "404.html", status=404))


def handler500(request):
    return(render(request, "500.html", status=500))

