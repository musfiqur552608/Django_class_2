
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pulls.urls')),
    path('admin/', admin.site.urls),
]
