from django.shortcuts import render
import random

# Create your views here.
def dice_roller(request, *args, **kwargs):
    random_number = None
    dyce_type = None  # Default to a six-sided die

    if request.method == 'POST':
        dice_type = request.POST.get("dice_type")

        dice_faces = {
            "d4": 4,
            "d6": 6,
            "d8": 8,
            "d10": 10,
            "d12": 12,
            "d20": 20,
            "d100": 100,
        }

        if dice_type in dice_faces:
            random_number = random.randint(1, dice_faces[dice_type])

    return render(request, 'dice/dice_roller.html',{
        'random_number': random_number,
        'dice_type': dyce_type
        })

