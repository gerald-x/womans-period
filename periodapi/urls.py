from django.urls import path
from . import views

urlpatterns = [
    path("create-cycles", views.create_cycles, name="create_cycles"),
    path("cycle-event", views.cycle_event, name="cycle_event")
]