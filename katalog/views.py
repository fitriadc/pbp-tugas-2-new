from django.shortcuts import render
from katalog.models import CatalogItem


def show_catalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'name': 'Fitria Dwi Cahya',
        'studentId': "2106751410"
    }
    return render(request, "katalog.html", context)
