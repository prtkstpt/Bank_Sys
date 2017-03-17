from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Bank.display),
    url(r'^customer/$', views.Customer.menu),
    url(r'^customer/create/$', views.Customer.create)
]
