from django.db.models import Q
from django.shortcuts import render
from catalog.models import Item  
def search_items(request):
    if request.method == 'GET':
        item_name = request.GET.get('item_name', '')

        items = Item.objects.filter(name__icontains=item_name)

        context = {
            'items': items,
            'item_name': item_name,
        }

        return render(request, 'search/search_results.html', context)
