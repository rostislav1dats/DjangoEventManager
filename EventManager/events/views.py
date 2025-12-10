# from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # organizer see only own events
        return Event.objects.filter(organizer=self.request.user)

    def perform_create(self, serializer):
        # set organizer automaticaly
        serializer.save(organizer=self.request.user)
