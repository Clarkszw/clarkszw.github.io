from django.urls import path
# to specify in the current folder to differ from other dependency called `views`
from . import views

# /products
# /products/1/detal
# /products/new

urlpatterns = [
    path('', views.index),
    path('new', views.new)

]
