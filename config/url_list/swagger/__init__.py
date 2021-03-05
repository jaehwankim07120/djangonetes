from .v1 import get_urlpatterns as v1_get_urlpatterns
from .v2 import get_urlpatterns as v2_get_urlpatterns


def get_urlpatterns():
    return v1_get_urlpatterns() + v2_get_urlpatterns()
