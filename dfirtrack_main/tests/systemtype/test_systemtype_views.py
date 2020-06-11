from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Systemtype
import urllib.parse

class SystemtypeViewTestCase(TestCase):
    """ systemtype view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Systemtype.objects.create(systemtype_name='systemtype_1')
        # create user
        test_user = User.objects.create_user(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')

    def test_systemtype_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemtype/', safe='')
        # get response
        response = self.client.get('/systemtype/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemtype_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemtype_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemtype/systemtype_list.html')

    def test_systemtype_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemtype')

    def test_systemtype_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # create url
        destination = urllib.parse.quote('/systemtype/', safe='/')
        # get response
        response = self.client.get('/systemtype', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_systemtype_detail_not_logged_in(self):
        """ test detail view """

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemtype/' + str(systemtype_1.systemtype_id) + '/', safe='')
        # get response
        response = self.client.get('/systemtype/' + str(systemtype_1.systemtype_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemtype_detail_logged_in(self):
        """ test detail view """

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/' + str(systemtype_1.systemtype_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemtype_detail_template(self):
        """ test detail view """

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/' + str(systemtype_1.systemtype_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemtype/systemtype_detail.html')

    def test_systemtype_detail_get_user_context(self):
        """ test detail view """

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/' + str(systemtype_1.systemtype_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemtype')

    def test_systemtype_detail_redirect(self):
        """ test detail view """

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # create url
        destination = urllib.parse.quote('/systemtype/' + str(systemtype_1.systemtype_id) + '/', safe='/')
        # get response
        response = self.client.get('/systemtype/' + str(systemtype_1.systemtype_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_systemtype_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemtype/add/', safe='')
        # get response
        response = self.client.get('/systemtype/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemtype_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemtype_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemtype/systemtype_add.html')

    def test_systemtype_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemtype')

    def test_systemtype_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # create url
        destination = urllib.parse.quote('/systemtype/add/', safe='/')
        # get response
        response = self.client.get('/systemtype/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_systemtype_edit_not_logged_in(self):
        """ test edit view """

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemtype/' + str(systemtype_1.systemtype_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/systemtype/' + str(systemtype_1.systemtype_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemtype_edit_logged_in(self):
        """ test edit view """

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/' + str(systemtype_1.systemtype_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemtype_edit_template(self):
        """ test edit view """

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/' + str(systemtype_1.systemtype_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemtype/systemtype_edit.html')

    def test_systemtype_edit_get_user_context(self):
        """ test edit view """

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtype/' + str(systemtype_1.systemtype_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemtype')

    def test_systemtype_edit_redirect(self):
        """ test edit view """

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # create url
        destination = urllib.parse.quote('/systemtype/' + str(systemtype_1.systemtype_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/systemtype/' + str(systemtype_1.systemtype_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
