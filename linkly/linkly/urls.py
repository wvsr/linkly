from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homePage, name="home"),
    path("<str:slug>/", views.shortUrl, name="url")
]
