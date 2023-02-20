from django.urls import path
from . import views
app_name='ecom'
urlpatterns = [
    path("",views.Home.as_view(),name='home'),
    path('register/',views.SignupSel,name='signup'),
    path('login/',views.signinseller,name='signin'),
    path("logout/",views.logouts,name='signout'),
    path("product/<int:pk>",views.Addproduct.as_view(),name='addproduct'),
    path("product/update/<int:pk>",views.Upproduct.as_view(),name='upproduct'),
    path("product/delete/<int:pk>",views.Delproduct.as_view(),name='delproduct'),
    path("subcategory/productview/<int:pk>",views.Subdetail.as_view(),name='detail'),
]