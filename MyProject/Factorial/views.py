# factorial_app/views.py

from django.shortcuts import render
from math import factorial

def index(request):
    result = None
    if request.method == 'POST':
        number = int(request.POST.get('number'))
        if 1 <= number <= 10:
            result = factorial(number)
    return render(request, 'Factorial/index.html', {'result': result})


