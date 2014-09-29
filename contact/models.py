# Django Modules
from django.db import models

# App Modules
from accounts.models import User


class Conversation(models.Model):
    """
    Convesation
    """
    sender = models.ForeignKey(User, related_name='conversation_sender')
    receiver = models.ForeignKey(User, related_name='conversation_receiver')
    seen = models.BooleanField(default=False, null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=False)
    deleted = models.BooleanField(default=False, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_deleted = models.DateTimeField(blank=True, null=True, auto_now_add=False, auto_now=False)

    def __str__(self):
        return '%s %s and %s %s' % (self.sender.first_name, self.sender.last_name, self.receiver.first_name, self.receiver.last_name)


class Message(models.Model):
    """
    Message
    """
    conversation = models.ForeignKey(Conversation, related_name='conversation')
    sender = models.ForeignKey(User, related_name='message_sender')
    receiver = models.ForeignKey(User, related_name='message_receiver')
    message = models.CharField(max_length=10000, null=False, blank=False)
    seen = models.BooleanField(default=False, null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=False)
    deleted = models.BooleanField(default=False, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_deleted = models.DateTimeField(blank=True, null=True, auto_now_add=False, auto_now=False)

    def __str__(self):
        return '%s %s and %s %s' % (self.sender.first_name, self.sender.last_name, self.receiver.first_name, self.receiver.last_name)
