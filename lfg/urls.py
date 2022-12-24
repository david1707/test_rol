from django.urls import path

from .views import LFGDetail, LFGList

urlpatterns = [
    path("lfg/<int:pk>/", LFGDetail.as_view(), name="lfg_detail"),
    path("lfg/", LFGList.as_view(), name="lfg_list"),
]
