from django.urls import path
from .views import ContactUser, MessagesListView

urlpatterns = [
    path('', ContactUser.as_view(), name='home'),
    path('xabarlar/', MessagesListView.as_view(), name='xabarlar')
]