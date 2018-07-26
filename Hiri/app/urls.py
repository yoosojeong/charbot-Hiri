from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^keyboard/$',
        view=views.Keyboard.as_view(),
        name='Keyboard',
    ),
    url(
        regex=r'^message$',
        view=views.Message.as_view(),
        name='Message',
    ),
]