from django.shortcuts import render
from django.template import RequestContext

def bad_request_page(request, exception=None):
    response = render(request, 'errors/400.html', {})
    response.status_code = 400
    
    return response


def permission_denied_page(request, exception=None):
    response = render(request, 'errors/403.html', {})
    response.status_code = 403

    return response


def page_not_found_page(request, exception=None):
    response = render(request, 'errors/404.html', {})
    response.status_code = 404
    
    return response


def server_error_page(request, exception=None):
    response = render(request, 'errors/500.html', {})
    response.status_code = 500

    return response

def server_unavailable_page(request, exception=None):
    response = render(request, 'errors/503.html', {})
    response.status_code = 503

    return response
