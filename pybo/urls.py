from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('adminfile/', include('adminfile.urls')),
    path('<str:pagename>', views.search1),
]