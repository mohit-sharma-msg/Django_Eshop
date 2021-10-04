from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.orders import OrderView
from .views.checkout import Checkout
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('checkout', Checkout.as_view(), name='checkout'),
]