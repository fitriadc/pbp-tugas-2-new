from django.test import TestCase, Client

# Create your tests here.


class MyWatchListTest(TestCase):
    def test_url_html(self):
        res = Client().get('/mywatchlist/html/')
        self.assertEqual(res.status_code, 200)

    def test_url_json(self):
        res = Client().get('/mywatchlist/json/')
        self.assertEqual(res.status_code, 200)

    def test_url_xml(self):
        res = Client().get('/mywatchlist/xml/')
        self.assertEqual(res.status_code, 200)
