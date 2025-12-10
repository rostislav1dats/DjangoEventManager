from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiuser/', include('users.urls')),
    path('apievents/', include('events.urls')),
]
