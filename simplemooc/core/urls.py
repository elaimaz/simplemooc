from django.urls import include, path

from simplemooc.core.views import contact, home

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contact, name='contact'),
]
