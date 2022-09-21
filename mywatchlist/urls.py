# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import mywatchlist_xml
from mywatchlist.views import mywatchlist_json
from mywatchlist.views import mywatchlist_by_id_json
from mywatchlist.views import mywatchlist_by_id_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', mywatchlist_xml, name='mywatchlist_xml'),
    path('json/', mywatchlist_json, name='mywatchlist_json'),
    path('json/<int:id>', mywatchlist_by_id_json,
         name='mywatchlist_by_id_json'),
    path('xml/<int:id>', mywatchlist_by_id_xml,
         name='mywatchlist_by_id_xml'),
]
