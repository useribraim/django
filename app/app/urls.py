from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(_('admin/'), admin.site.urls),
]

urlpatterns += i18n_patterns (
    path('api/', include('app_api.urls')),
    #path('', include('lang.urls', namespace='lang')),
    path('', include('first.urls'))
)
# urlpatterns += [
    
# ]
