from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Category, Comments, Basket
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse


def index(request):
    return render(request, 'main/index.html')
#start

def products(request):
    print('start')
    Books = Book.objects.all()
    return render(request, "main/products.html", {'Books': Books})

def getProduct(request, book_id):
    book = Book.objects.get(id=book_id)
    print(book.book_img)
    comments = Comments.objects.filter(book=book)
    return render(request, "main/book.html", {'Book': book, 'Comment': comments})

def getComment(request, book_id):
    content = request.POST['comment']
    date = timezone.now()
    current_user = request.user
    book = Book.objects.get(id=book_id)
    print(current_user.id)
    if content != "":
        newComment = Comments(date_create=date, content=content, creator_user=current_user, book=book)
        newComment.save()
    return HttpResponseRedirect('/')


def category(request):
    category = Category.objects.all()
    return render(request, "main/category.html", {'Categories': category})

def getCategory(request, category_id):
    Books = Book.objects.filter(category=category_id)
    Book_Category = Category.objects.get(id=category_id)
    
    return render(request, "main/categoryProducts.html", {
        'Books'         : Books,
        'Book_Category' : Book_Category.category_name,
        'Book_Id'       : Book_Category.id
    })


def contactform(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            message = request.POST['message']
            send_mail(request.user.username, message, settings.EMAIL_HOST_USER, ['nikita.worker000@gmail.com'])
            return render(request, 'main/contact.html')
        else:
            return render(request, 'login/authorization.html', {'error': 'Авторизируйтесь, чтобы отправить отзыв'})

    return render(request, 'main/contact.html')

def basket(request):
    baskets = Basket.objects.filter(user=request.user)
    book = []
    for basket in baskets:
        book.append(Book.objects.filter(id=basket.book_id))

    for booken in baskets:
        print(booken.Book.book_name)
    content = {'basket':baskets, 'books':book}
    return render(request, 'basketapp/basket.html', content)


def basketAdd(request, pk):
    book = get_object_or_404(Book, pk=pk)
    basket = Basket.objects.filter(user=request.user, book=book).first()
    if not basket:
        basket = Basket(user=request.user, book=book)
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(reverse('contentLoader:basket'))


def basket_remove(request, pk):
    content = {}
    return render(request, 'basketapp/basket.html', content)