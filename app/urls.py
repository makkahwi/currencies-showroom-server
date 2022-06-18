from django.urls import path, re_path
from django.views.generic.base import RedirectView
from rest_framework_simplejwt import views as jwt_views

from app.viewset import (
    CurrencyListView,
    CurrencyCreateView,
    CurrencyDetailView,
    CurrencyUpdateView,
    CurrencyDestroyView,
)

urlpatterns = [
    path("token/obtain", jwt_views.TokenObtainPairView.as_view(), name="JWT Obtain"),
    path("token/refresh", jwt_views.TokenRefreshView.as_view(), name="JWT Refresh"),
    path("api/v1/currencies/", CurrencyListView.as_view(), name="Currency API List"),
    path(
        "api/v1/currencies/create",
        CurrencyCreateView.as_view(),
        name="Currency API Create",
    ),
    path(
        "api/v1/currencies/<int:pk>",
        CurrencyDetailView.as_view(),
        name="Currency API Detail",
    ),
    path(
        "api/v1/currencies/<int:pk>/update",
        CurrencyUpdateView.as_view(),
        name="Currency API Update",
    ),
    path(
        "api/v1/currencies/<int:pk>/delete",
        CurrencyDestroyView.as_view(),
        name="Currency API Delete",
    ),
    re_path(
        r"^.*$",
        RedirectView.as_view(url="api/v1/currencies/", permanent=False),
        name="Redirect",
    ),
]
