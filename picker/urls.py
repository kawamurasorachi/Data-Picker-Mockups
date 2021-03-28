from django.urls import path
from .views import TopView, HomeView

app_name = 'picker'
urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('<slug:username>/', HomeView.as_view(), name='home'),
]
