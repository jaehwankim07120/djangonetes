from django.contrib import admin
from django.conf.urls import url, include 
from django.urls import path


from service.views import errors as errors_view


def get_urlpatterns():


    return [
        url(r'^400/', errors_view.bad_request_page),
        url(r'^403/', errors_view.permission_denied_page),
        url(r'^404/', errors_view.page_not_found_page),
        url(r'^500/', errors_view.server_error_page),
        url(r'^503/', errors_view.server_unavailable_page),
    ]

