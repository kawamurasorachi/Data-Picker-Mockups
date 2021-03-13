from django.urls import path
from .views import IndexView

app_name='picker'

urlpatterns = [
    path('', IndexView.as_view(), name='top'),
]
