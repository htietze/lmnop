from django.test import TestCase
from lmnop_project import helpers
from ..models import Artist, Venue, Show


# test will take a small sample of data using the pg_records function and assertequals
class TestListWithPageData(TestCase):

    def setUp(self):
        for i in range(3):
            artist = Artist(name=f'Number{i+1}')
            artist.save()  # must save the new artist, then get id
            venue = Venue(name=f'venue{i+1}', city=f'city{i+1}', state=f'state{i+1}')
            venue.save()

    # check that names returned from db are correct on first loaded page
    def test_first_page_correct_entries_artist(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(1, artists, 2)
        self.assertEqual(artists[0].name, paged_list[0].name)
        self.assertEqual(artists[1].name, paged_list[1].name)

    # check that names returned from db are correct on second loaded page
    def test_second_page_correct_entries_artist(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(2, artists, 2)
        self.assertEqual(artists[2].name, paged_list[0].name)

    # check that the desired number of items are displayed per page
    def test_correct_number_of_items_returned_page_one_artist(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(1, artists, 2)
        self.assertEqual(len(paged_list), 2)

    # check that the desired number of items are displayed per page
    def test_correct_number_of_items_returned_page_two_artist(self):
        artists = Artist.objects.all().order_by('name')
        paged_list = helpers.pg_records(2, artists, 2)
        self.assertEqual(len(paged_list), 1)

    # check that goes to last page when page entered is higher than number of existing pages
    def test_page_number_higher_than_exists(self):
        artists = Artist.objects.all().order_by('name')
        paged_list_exists = helpers.pg_records(2, artists, 2)
        paged_list_out_of_bounds = helpers.pg_records(4000, artists, 2)
        self.assertEquals(str(paged_list_exists), str(paged_list_out_of_bounds))
        paged_list_out_of_bounds = helpers.pg_records(10000, artists, 2)
        self.assertEquals(str(paged_list_exists), str(paged_list_out_of_bounds))
        paged_list_out_of_bounds = helpers.pg_records(50000, artists, 2)
        self.assertEquals(str(paged_list_exists), str(paged_list_out_of_bounds))
        paged_list_out_of_bounds = helpers.pg_records(100000, artists, 2)
        self.assertEquals(str(paged_list_exists), str(paged_list_out_of_bounds))

    def test_page_number_lower_than_exists(self):
        artists = Artist.objects.all().order_by('name')
        paged_list_exists = helpers.pg_records(1, artists, 2)
        paged_list_out_of_bounds = helpers.pg_records(-5, artists, 2)
        self.assertEquals(str(paged_list_exists), str(paged_list_out_of_bounds))
        paged_list_out_of_bounds = helpers.pg_records(-10, artists, 2)
        self.assertEquals(str(paged_list_exists), str(paged_list_out_of_bounds))
        paged_list_out_of_bounds = helpers.pg_records(-100, artists, 2)
        self.assertEquals(str(paged_list_exists), str(paged_list_out_of_bounds))
        paged_list_out_of_bounds = helpers.pg_records(-1000, artists, 2)
        self.assertEquals(str(paged_list_exists), str(paged_list_out_of_bounds))

