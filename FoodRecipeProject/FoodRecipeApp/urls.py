from django.contrib import admin
from django.urls import path
from .views import ReceipeApi,ReceipeModifyApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/receipe/', ReceipeApi.as_view(), name="api-view-receipe"),
    path('api/receipe/<str:pk>', ReceipeModifyApi.as_view(), name="api-modify-receipe"),
]
