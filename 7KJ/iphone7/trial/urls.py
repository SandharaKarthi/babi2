from django.urls import path
from trial import views 

urlpatterns = [

    path("t1/",views.greens,name="t1"),
    path("t2/",views.blue,name="t2"),
]