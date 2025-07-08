from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index),
    path("categories/<cat>", views.categories),
    path("detailpro/<slug>", views.detailpage),
    path("cart", views.showCart),
    path("search", views.search),
    path("signin", views.signin),
    path("signup", views.signup),
    path("logout", views.logout_user),
    path("order", views.showOrderPage),
    path("payment", views.payment_success),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
