from . import views
from django.urls import path
app_name = 'shop'

urlpatterns = [

    # path('',views.base,name='base'),
    path('',views.allproductCat,name='allproductCat'),
    path('<slug:c_slug>/',views.allproductCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productDetail,name='productdetails')

]