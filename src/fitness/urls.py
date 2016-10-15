from django.conf.urls import url

from fitness.views import *

urlpatterns = [
    url(r'^fitness', bmi_view),
    url(r'^$', bmi_view),
    url(r'^workout/', workout_view)
]