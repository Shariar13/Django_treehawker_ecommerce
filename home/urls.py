from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views



urlpatterns = [
   
    path('',views.home,name='home'),
    path('signinn/',views.signinn,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('signout/',views.signout,name="signout"),
    path('review/<int:pk>',views.review.as_view(),name="review"),
    path('review_form/',views.review_form,name="review_form"),
    path('contact/',views.contact,name="contact"),
    path('contact_form/',views.contact_form,name="contact_form"),
    path('garden/',views.garden.as_view(),name="garden"),
    path('fruit/',views.fruit.as_view(),name="fruit"),
    path('vegetable/',views.vegetable.as_view(),name="vegetable"),
    path('flower/',views.flower.as_view(),name="flower"),
    path('tree/',views.tree.as_view(),name="tree"),
    path('cart/',views.cart.as_view(),name="cart"),
    path('cart_form/',views.cart_form,name="cart_form"),
    path('blog/',views.blog.as_view(),name="blog"),
    path('blog_details/<int:pk>',views.blog_details.as_view(),name="blog_details"),
    path('portfolio/',views.portfolio.as_view(),name="portfolio"),
    path('make_your_garden/',views.make_your_garden.as_view(),name="make_your_garden"),
    path('make_your_garden_corporate/',views.make_your_garden_corporate.as_view(),name="make_your_garden_corporate"),
    path('make_your_garden_balcony/',views.make_your_garden_balcony.as_view(),name="make_your_garden_balcony"),
    path('create_your_garden/',views.create_your_garden,name="create_your_garden"),
    path('my_garden/',views.my_garden.as_view(),name="my_garden"),
    path('about/',views.about.as_view(),name="about"),
    path('payment/<int:pk>',views.payment.as_view(),name="payment"),
    path('order_form',views.order_form,name="order_form"),
    path('<int:pk>/remove_cart',views.remove_cart.as_view(),name="remove_cart"),
    path('payment_all',views.payment_all.as_view(),name="payment_all"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = 'password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'),name='password_reset_complete'),  
    

    


    
    
  
]