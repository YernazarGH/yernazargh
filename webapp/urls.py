from django.urls import path
from webapp.views import ListTariffView, index_view, CreateMyTariffView, DetailTariffView
urlpatterns = [
    path('tariffs', ListTariffView.as_view(), name='tariff_list'),
    path('', index_view, name='main'),
    path('tariff/<int:pk>/create/mytariff', CreateMyTariffView.as_view(), name='create_mytariff'),
    path('tariff/<int:pk>/', DetailTariffView.as_view(), name='tariff_detail'),
]
