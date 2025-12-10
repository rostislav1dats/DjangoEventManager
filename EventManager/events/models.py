from django.db import models
from django.conf import settings

class Event(models.Model):
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organized_events',
        db_index=True                       # fast view events by organizer
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(db_index=True) # cuz sorting and searching via date
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        indexes = [
            models.Index(fields=['organizer', 'date']),
        ]

    def __str__(self):
        return f'{self.title} - {self.organizer.email}'
