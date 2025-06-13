from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nuzlocke_tracker/', include('nuzlocke_tracker.urls'))
]
