from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Location
import urllib.parse

class LocationViewTestCase(TestCase):
    """ location view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Location.objects.create(location_name='location_1')
        # create user
        test_user = User.objects.create_user(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')

    def test_location_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/location/', safe='')
        # get response
        response = self.client.get('/location/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_location_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_location_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/location/location_list.html')

    def test_location_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_location')

    def test_location_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # create url
        destination = urllib.parse.quote('/location/', safe='/')
        # get response
        response = self.client.get('/location', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_location_detail_not_logged_in(self):
        """ test detail view """

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/location/' + str(location_1.location_id) + '/', safe='')
        # get response
        response = self.client.get('/location/' + str(location_1.location_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_location_detail_logged_in(self):
        """ test detail view """

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/' + str(location_1.location_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_location_detail_template(self):
        """ test detail view """

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/' + str(location_1.location_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/location/location_detail.html')

    def test_location_detail_get_user_context(self):
        """ test detail view """

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/' + str(location_1.location_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_location')

    def test_location_detail_redirect(self):
        """ test detail view """

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # create url
        destination = urllib.parse.quote('/location/' + str(location_1.location_id) + '/', safe='/')
        # get response
        response = self.client.get('/location/' + str(location_1.location_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_location_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/location/add/', safe='')
        # get response
        response = self.client.get('/location/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_location_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_location_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/location/location_add.html')

    def test_location_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_location')

    def test_location_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # create url
        destination = urllib.parse.quote('/location/add/', safe='/')
        # get response
        response = self.client.get('/location/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_location_edit_not_logged_in(self):
        """ test edit view """

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/location/' + str(location_1.location_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/location/' + str(location_1.location_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_location_edit_logged_in(self):
        """ test edit view """

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/' + str(location_1.location_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_location_edit_template(self):
        """ test edit view """

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/' + str(location_1.location_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/location/location_edit.html')

    def test_location_edit_get_user_context(self):
        """ test edit view """

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/location/' + str(location_1.location_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_location')

    def test_location_edit_redirect(self):
        """ test edit view """

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # create url
        destination = urllib.parse.quote('/location/' + str(location_1.location_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/location/' + str(location_1.location_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
