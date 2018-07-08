from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^keyboard/$',
        view=views.Keyboard.as_view(),
        name='Keyboard',
    ),
]