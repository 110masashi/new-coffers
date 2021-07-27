from django.contrib import admin
from django.urls import path
from .views import IndexView, BeansView, EquipmentView, WaterView, ArrangeView , SignupView , BlogList, BlogDetail #, Beans_BuyView, Equipment_BuyView, Water_BuyView

urlpatterns = [
    path('', IndexView.as_view()),
    path('beans/', BeansView.as_view()),
    path('equipment/', EquipmentView.as_view()),
    path('water/', WaterView.as_view()),
    path('arrange/', ArrangeView.as_view()),
    path('list/', BlogList.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='detail'),
    path('signup/', SignupView.as_view()),
    # path('beans_buy/', Beans_BuyView.as_view()),
    # path('equipment_buy/', Equipment_BuyView.as_view()),
    # path('water_buy/', Water_BuyView.as_view()),
]