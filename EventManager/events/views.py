# from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer
from .filters import EventFilter


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = EventFilter
    # fields for ordering
    ordering_fields = ['date', 'created_at']

    def get_queryset(self):
        # organizer see only own events
        return Event.objects.filter(organizer=self.request.user)

    def perform_create(self, serializer):
        # set organizer automaticaly
        serializer.save(organizer=self.request.user)
