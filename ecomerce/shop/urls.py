
from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    path('',views.allProductCat,name="allProductCat"),
    path('<slug:c_slug>/',views.allProductCat,name="products_by_catogory"),
    path('<slug:c_slug>/<slug:product_slug>/', views.productdetails, name='productdetails'),
    ]