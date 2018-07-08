from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/', include(('app.urls', 'app'), namespace='app')),
]
