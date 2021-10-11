from django.urls import path

from . import views
#app_name = 'bank'
urlpatterns = [
    path('', views.index, name='index'),
    path('transaction', views.transaction, name='transaction'),
    path('register',views.register, name='register'),
    path('customers',views.customers, name='customers'),
    path('transfer',views.transfer, name='transfer')
]