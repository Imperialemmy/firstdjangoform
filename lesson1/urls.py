from django.urls import path
from . import views

urlpatterns = [
    path ('',views.display ),
    path ('models',views.displayModels),
    path ('models.html',views.displayModels)
]
