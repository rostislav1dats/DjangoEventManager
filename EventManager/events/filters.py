import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')  # частичное совпадение
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    date_after = django_filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    date_before = django_filters.DateTimeFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['location', 'title', 'date_after', 'date_before']
        