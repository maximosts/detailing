import statistics
from django.contrib import admin
from django.urls import path, include
from main import views as main_views
from catalog import views as catalog_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),  # Homepage from the "main" app
    path('catalog/', include('catalog.urls')),  # URL patterns from the "catalog" app
    path('', include('search.urls')),
    path('accounts/', include('accounts.urls')),
    path('comments/', include('comments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
