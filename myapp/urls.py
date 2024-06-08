from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
     path("home", views.home, name="home"),



    path("shop1", views.shop1, name="shop1"),
    path("shop2", views.shop2, name="shop2"),


    path("shop1_products",views.shop1_products,name="shop1_products"),
    path("shop2_products", views.shop2_products, name="shop2_products"),
    path("path2/<str:id1>", views.productinfo, name="productinfo"),
    path("path3/<int:id1>/", views.productinfos, name="productinfos"),
                  path('signinz', views.signin, name='signin'),
                  path('signupz', views.signup, name='signup'),
                  path('loutz', views.lout, name='lout'),
    path("about",views.about,name="about"),

                  path('cartz', views.cart, name='cart'),
                  path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
                  path('remove_from_cart/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
path('checkoutz', views.checkout, name='checkout'),
path('order-successz', views.order_success, name='order_success'),
                  path('show_bill/', views.show_bill, name='show_bill'),
                  path("contact",views.contacts,name="contacts"),
    path("contact_success",views.contact_success,name="contact_success")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

