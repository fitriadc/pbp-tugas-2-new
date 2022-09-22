# Create your views here.

from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers


def show_mywatchlist(request):
    mywatchlist_data = MyWatchList.objects.all()
    countWatched = 0
    countNotWatched = 0

    # Fitur untuk menampilkan pesan
    message = ""

    # Menghitung jumlah film yang telah ditonton
    for alreadyWatched in mywatchlist_data:
        if (alreadyWatched.watched == True):
            countWatched += 1
        else:
            countNotWatched += 1

    if (countWatched >= countNotWatched):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        'data_mywatchlist': mywatchlist_data,
        'name': 'Fitria Dwi Cahya',
        'studentId': "2106751410",
        'message': message,
    }
    return render(request, "mywatchlist.html", context)


# Mengembalikan data dalam bentuk XML


def mywatchlist_xml(request):
    mywatchlist_data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", mywatchlist_data), content_type="application/xml")

# Mengembalikan data dalam bentuk JSON


def mywatchlist_json(request):
    mywatchlist_data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", mywatchlist_data), content_type="application/json")


# Mengembalikan data dalam bentuk XML berdasarkan id


def mywatchlist_by_id_xml(request, id):
    mywatchlist_data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", mywatchlist_data), content_type="application/xml")

# Mengembalikan data dalam bentuk JSON berdasarkan id


def mywatchlist_by_id_json(request, id):
    mywatchlist_data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", mywatchlist_data), content_type="application/json")
