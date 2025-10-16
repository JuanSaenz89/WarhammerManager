from django.shortcuts import render

# Create your views here.
def faction_list(request):
    return render(request, 'factions/faction_list.html')