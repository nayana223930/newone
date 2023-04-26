from django.urls import path
from . import views
urlpatterns=[
    path("",views.new,name="ent"),
    path("reg",views.register,name="reg"),
    path("login",views.login,name="login"),
    path("bio",views.detail,name="bio"),
    path("logout",views.logout,name="logout"),
    path("about",views.about,name='about'),
    path("contact",views.contact,name="contact")
]