from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemCreatorViewTestCase(TestCase):
    """ system creator view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_creator', password='Jbf5fZBhpg1aZsCW6L8r')

    def test_system_creator_not_logged_in(self):
        """ test creator view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/creator/', safe='')
        # get response
        response = self.client.get('/system/creator/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_creator_logged_in(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_system_creator', password='Jbf5fZBhpg1aZsCW6L8r')
        # get response
        response = self.client.get('/system/creator/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_creator_template(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_system_creator', password='Jbf5fZBhpg1aZsCW6L8r')
        # get response
        response = self.client.get('/system/creator/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_creator.html')

    def test_system_creator_get_user_context(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_system_creator', password='Jbf5fZBhpg1aZsCW6L8r')
        # get response
        response = self.client.get('/system/creator/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_creator')

    def test_system_creator_redirect(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_system_creator', password='Jbf5fZBhpg1aZsCW6L8r')
        # create url
        destination = urllib.parse.quote('/system/creator/', safe='/')
        # get response
        response = self.client.get('/system/creator', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
