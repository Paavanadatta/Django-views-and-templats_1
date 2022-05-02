from django.urls import path
from demo3_1 import views
urlpatterns=[
    path("f3/", views.f3,name="f3"),
    path("f4/", views.f4,name="f4"),
    path("f5/", views.f5,name="f5"),
    path("f6/<data>/", views.f6,name="f6"),
    path("f7/", views.f7,name="f7"),
    path("f8/", views.f8,name="f8"),
    path("f9/", views.f9,name="f9"),
    path("f11/", views.f11,name="f11"),
    path("f14/", views.f14,name="f14"),
    path("f15/", views.f15,name="f15")


]