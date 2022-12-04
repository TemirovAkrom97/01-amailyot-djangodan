from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Contact
from django.urls import reverse_lazy

# Create your views here.
class ContactUser(CreateView):
    model = Contact
    fields = ('first_name', 'last_name', 'phone_num', 'email', 'message',)
    success_url = reverse_lazy('xabarlar')
    template_name = 'home.html'

class MessagesListView(ListView):
    model = Contact
    template_name = 'messages.html'