from .models import Message, Project 
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Message
    fields = [ 
      "id", 
      "sender_name",
      "sender_email",
      "subject", 
      "text_body"
    ]

class ProjectSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Project
    fields = [
      "id",
      "title",
      "skills",
      "images",
      "description"
    ]

