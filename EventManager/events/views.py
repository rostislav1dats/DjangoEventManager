# from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer
from .filters import EventFilter
from .tasks import send_event_email


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
        event = serializer.save(organizer=self.request.user)

        # call celery task
        send_event_email(
            organizer_email=event.organizer.email,
            title=event.title,
            date=event.date.strftime('%Y-%m-%d %H:%M'),
            location=event.location
        )
