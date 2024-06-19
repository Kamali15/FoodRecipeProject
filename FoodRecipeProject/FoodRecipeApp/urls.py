from django.contrib import admin
from django.urls import path
from .views import ReceipeApi,ReceipeModifyApi

urlpatterns = [
    path('admin/', admin.site.urls),
    # {% comment %} path('recipes/', FoodRecipeListCreateView.as_view(), name='recipe-list-create'),
    # path('recipes/<int:pk>/', FoodRecipeUpdateView.as_view(), name='recipe-update'), {% endcomment %}
    path('api/receipe/', ReceipeApi.as_view(), name="api-view-receipe"),
    path('api/receipe/<str:pk>', ReceipeModifyApi.as_view(), name="api-modify-receipe"),
]
