from django.contrib import admin
from django.urls import path

from core.project.settings import ADMIN_PATH

urlpatterns = [
    path(f'{ADMIN_PATH}/', admin.site.urls),
]
