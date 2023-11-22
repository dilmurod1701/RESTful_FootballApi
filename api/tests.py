from django.test import TestCase
from rest_framework.test import APIClient
from selenium import webdriver

# Local application packages
from .models import Game

# Create your tests here.


class TestModels(TestCase):
    def setUp(self) -> None:
        Game.objects.create(home_team='Real Madrid', away_team='Barcelona', date='2023-11-10', hour='23:34 PM', venue='Amsterdam')
        Game.objects.create(home_team='Liverpool', away_team='Man City', date='2023-09-20', hour='21:00 PM', venue='Jakarta International Stadium')
        Game.objects.create(home_team='Chelsea', away_team='Man United', date='2022-04-14', hour='00:00 AM', venue='Goodison Park')
        Game.objects.create(home_team='PSG', away_team='Bavariya', date='2024-07-23', hour='23:00 PM', venue='Parc des Princes')

    def test_home_team(self):
        obj1 = Game.objects.get(home_team='Real Madrid')
        obj2 = Game.objects.get(home_team='Liverpool')
        obj3 = Game.objects.get(home_team='Chelsea')
        obj4 = Game.objects.get(home_team='PSG')
        self.assertEquals(obj1.home_team, 'Real Madrid')
        self.assertEquals(obj2.home_team, 'Liverpool')
        self.assertEquals(obj3.home_team, 'Chelsea')
        self.assertEquals(obj4.home_team, 'PSG')

    def test_away_team(self):
        obj1 = Game.objects.get(away_team='Barcelona')
        obj2 = Game.objects.get(away_team='Man City')
        obj3 = Game.objects.get(away_team='Man United')
        obj4 = Game.objects.get(away_team='Bavariya')
        self.assertEquals(obj1.away_team, 'Barcelona')
        self.assertEquals(obj2.away_team, 'Man City')
        self.assertEquals(obj3.away_team, 'Man United')
        self.assertEquals(obj4.away_team, 'Bavariya')

    def test_hour(self):
        obj1 = Game.objects.get(hour='23:34 PM')
        obj2 = Game.objects.get(hour='21:00 PM')
        obj3 = Game.objects.get(hour='00:00 AM')
        obj4 = Game.objects.get(hour='23:00 PM')
        self.assertEquals(obj1.hour, '23:34 PM')
        self.assertEquals(obj2.hour, '21:00 PM')
        self.assertEquals(obj3.hour, '00:00 AM')
        self.assertEquals(obj4.hour, '23:00 PM')

    def test_venue(self):
        obj1 = Game.objects.get(venue='Amsterdam')
        obj2 = Game.objects.get(venue='Jakarta International Stadium')
        obj3 = Game.objects.get(venue='Goodison Park')
        obj4 = Game.objects.get(venue='Parc des Princes')
        self.assertEquals(obj1.venue, 'Amsterdam')
        self.assertEquals(obj2.venue, 'Jakarta International Stadium')
        self.assertEquals(obj3.venue, 'Goodison Park')
        self.assertEquals(obj4.venue, 'Parc des Princes')


class TestView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        Game.objects.create(home_team='Real Madrid', away_team='Barcelona', date='2023-11-10', hour='23:34 PM', venue='Amsterdam')
        Game.objects.create(home_team='Liverpool', away_team='Man City', date='2023-09-20', hour='21:00 PM', venue='Jakarta International Stadium')
        Game.objects.create(home_team='Chelsea', away_team='Man United', date='2022-04-14', hour='00:00 AM', venue='Goodison Park')
        Game.objects.create(home_team='PSG', away_team='Bavariya', date='2024-07-23', hour='23:00 PM', venue='Parc des Princes')

    def test_site(self):
        response = self.client.get('http://127.0.0.1:8000/api/game')
        self.assertNotEquals(response.json()[0]['home_team'], response.json()[0]['away_team'])
        self.assertNotEquals(response.json()[0]['date'], response.json()[1]['date'])
        self.assertNotEquals(response.json()[2]['hour'], response.json()[3]['hour'])
        self.assertNotEquals(response.json()[1]['venue'], response.json()[0]['venue'])


class FootballSelenium(TestView):
    def setUp(self) -> None:
        self.client = APIClient()
        Game.objects.create(home_team='Real Madrid', away_team='Barcelona', date='2023-11-10', hour='23:34 PM', venue='Amsterdam')
        Game.objects.create(home_team='Liverpool', away_team='Man City', date='2023-09-20', hour='21:00 PM', venue='Jakarta International Stadium')
        Game.objects.create(home_team='Chelsea', away_team='Man United', date='2022-04-14', hour='00:00 AM', venue='Goodison Park')
        Game.objects.create(home_team='PSG', away_team='Bavariya', date='2024-07-23', hour='23:00 PM', venue='Parc des Princes')

    def test_view_page(self):
        self.client = APIClient()
        response = webdriver.Chrome()
        response.get('http://127.0.0.1:8000/api/game')
        assert 'home_team' in response.page_source
        assert 'away_team' in response.page_source
        assert 'date' in response.page_source
        assert 'hour' in response.page_source
        assert 'venue' in response.page_source

    def test_view_email(self):
        self.client = APIClient()
        response = webdriver.Chrome()
        response.get('http://127.0.0.1:8000/api/')
        assert 'email' in response.page_source
