from django.urls import path

from paintapp.views import ColorPickerView

urlpatterns = [
    # paint/
    path('', ColorPickerView.as_view(), name='paint')
]
