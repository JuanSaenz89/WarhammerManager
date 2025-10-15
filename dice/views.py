from django.shortcuts import render
import random

# Create your views here.
def dice_roller(request, *args, **kwargs):
    random_number = None
    dyce_type = None  # Default to a six-sided die

    if request.method == 'POST':
        dyce_type = request.POST.get('dice_type')

        if dyce_type == "d4":
            random_number = random.randint(1, 4)
        elif dyce_type == "d6":
            random_number = random.randint(1, 6)
        elif dyce_type == "d8":
            random_number = random.randint(1, 8)
        elif dyce_type == "d10":
            random_number = random.randint(1, 10)
        elif dyce_type == "d12":
            random_number = random.randint(1, 12)
        elif dyce_type == "d20":
            random_number = random.randint(1, 20)
        elif dyce_type == "d100":
            random_number = random.randint(1, 100)

    return render(request, 'dice/dice_roller.html',{
        'random_number': random_number,
        'dice_type': dyce_type
        })

