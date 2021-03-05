"""
    djangonetes URL Configuration
"""
from django.conf.urls.static import static
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
from config import url_list

urlpatterns = []

# admin
urlpatterns += url_list.admin.get_urlpatterns()

# rest api
urlpatterns += []

# swagger
urlpatterns += url_list.swagger.v1.get_urlpatterns()
urlpatterns += url_list.swagger.v2.get_urlpatterns()

# register - error pages
urlpatterns += url_list.pages.get_urlpatterns()

handler400 = 'service.views.errors.bad_request_page'
handler403 = 'service.views.errors.permission_denied_page'
handler404 = 'service.views.errors.page_not_found_page'
handler500 = 'service.views.errors.server_error_page'