from django.urls import path, include
from . import views

app_name = 'contentLoader'

urlpatterns = [
    path('', views.index, name = "index"),
    path('products/', views.products, name = "products"),
    path('products/<int:book_id>/', views.getProduct, name="getProduct"),
    path('category/', views.category, name="category"),
    path('category/<int:category_id>', views.getCategory, name="getCategories"),
    path('addComment/<int:book_id>', views.getComment, name='getComment'),
    path('contact/', views.contactform, name='contact'),
]