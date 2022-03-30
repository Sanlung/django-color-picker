from django.shortcuts import render
from django.views import View

from paintapp.forms import ColorPickerForm
# Create your views here.

class ColorPickerView(View):
    def get(self, request):
        """http GET request that present the color picker form"""
        form = ColorPickerForm()

        context = {
            'form': form,
            'red': 255,
            'green': 255,
            'blue': 255,
        }

        return render(request, 'paint.html', context=context)

    def post(self, request):
        """http POST request that sents user data to paint the page"""
        form = ColorPickerForm(request.POST)

        red = int(request.POST['red_amount'])
        green = int(request.POST['green_amount'])
        blue = int(request.POST['blue_amount'])

        context = {
            'form': form,
            'red': red,
            'green': green,
            'blue': blue,
        }

        return render(request, 'paint.html', context=context)
