from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # all products WITHOUT category
    path('', views.allProdCat, name='allProdCat'),
    # all products WITH category
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category' ),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'),
]
