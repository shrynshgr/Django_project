from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('contact/',views.table),
    path('signup/',views.signup),
    path('addrecord/',views.addrecord),
    path('delete/<int:id>/',views.delete),
    path('update/<int:id>/',views.update),
    path('updaterecord/<int:id>/',views.updaterecord),

]