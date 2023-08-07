from django.views.generic import ListView
from ..models import House

class HouseListView(ListView):
     model = House