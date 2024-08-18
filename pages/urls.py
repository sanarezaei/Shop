from django.urls import path
from .views import HomePageView, AboutUsPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('aboutus/', AboutUsPageView.as_view(), name='aboutus'),
]

