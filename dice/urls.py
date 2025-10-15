
from django.urls import path
from .views import dice_roller


urlpatterns = [
    path('', dice_roller, name='dice_roller'),
]
