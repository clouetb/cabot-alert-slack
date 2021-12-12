from django.urls import re_path
from .views import slack_message_callback

urlpatterns = [
    re_path(r'^messages', slack_message_callback, name="slack-message-callback"),
]
