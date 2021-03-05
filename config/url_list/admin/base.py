from django.contrib import admin
from django.conf.urls import url, include 
from django.urls import path

def get_urlpatterns():
    return [
        path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
        path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
        #url(r'^admin/', admin.site.urls),
        url(r'^', admin.site.urls),
    ]
