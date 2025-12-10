from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.EmailField(source='organizer.email', read_only=True)
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('organizer', 'created_at', 'update_at')