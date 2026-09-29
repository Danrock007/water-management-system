from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
    path('sales/', include('sales.urls')),
    path('inventory/', include('inventory.urls')),
    path('logistics/', include('logistics.urls')),
    path('finance/', include('finance.urls')),
    path('dashboard/', include('dashboard.urls')),
]