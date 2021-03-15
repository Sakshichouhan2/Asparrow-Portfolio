from django.contrib import admin
from django.urls import path, include
from AsparrowApp import views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home', views.HomePageView.as_view(template_name="index.html"))
    path("home", views.home, name= "home"),
    path("portfolio", views.portfolio, name= "portfolio"),
    path("services", views.services, name= "services"),
    path("contact", views.contact, name= "contact"),
    path("about", views.about,name = "about"),
    path("career", views.career, name= "career")
]
