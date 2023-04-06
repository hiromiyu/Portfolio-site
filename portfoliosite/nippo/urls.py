from django.urls import path
from .views import nippoListView, nippoDetailView, nippoCreateView
from .contact import contactView
from .import views

app_name = 'nippo'
urlpatterns = [
    path("", contactView, name="nippo-contact"),
    # path("", nippoListView, name="nippo-list"),
    path("detail/<int:number>/", nippoDetailView, name="nippo-detail"),
    path("create/", nippoCreateView, name="nippo-create"),
    # path("contact/", contactView, name="nippo-contact"),
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
]