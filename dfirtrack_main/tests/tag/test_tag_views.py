from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Tag, Tagcolor
import urllib.parse

class TagViewTestCase(TestCase):
    """ tag view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tag_1')
        # create object
        Tag.objects.create(tag_name='tag_1', tagcolor = tagcolor_1)
        # create user
        test_user = User.objects.create_user(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')

    def test_tag_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tag/', safe='')
        # get response
        response = self.client.get('/tag/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tag_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tag_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/tag/tag_list.html')

    def test_tag_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_tag')

    def test_tag_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # create url
        destination = urllib.parse.quote('/tag/', safe='/')
        # get response
        response = self.client.get('/tag', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_tag_detail_not_logged_in(self):
        """ test detail view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tag/' + str(tag_1.tag_id) + '/', safe='')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tag_detail_logged_in(self):
        """ test detail view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tag_detail_template(self):
        """ test detail view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/tag/tag_detail.html')

    def test_tag_detail_get_user_context(self):
        """ test detail view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_tag')

    def test_tag_detail_redirect(self):
        """ test detail view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # create url
        destination = urllib.parse.quote('/tag/' + str(tag_1.tag_id) + '/', safe='/')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_tag_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tag/add/', safe='')
        # get response
        response = self.client.get('/tag/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tag_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tag_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/tag/tag_add.html')

    def test_tag_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_tag')

    def test_tag_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # create url
        destination = urllib.parse.quote('/tag/add/', safe='/')
        # get response
        response = self.client.get('/tag/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_tag_edit_not_logged_in(self):
        """ test edit view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tag/' + str(tag_1.tag_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tag_edit_logged_in(self):
        """ test edit view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tag_edit_template(self):
        """ test edit view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/tag/tag_edit.html')

    def test_tag_edit_get_user_context(self):
        """ test edit view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_tag')

    def test_tag_edit_redirect(self):
        """ test edit view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # create url
        destination = urllib.parse.quote('/tag/' + str(tag_1.tag_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_tag_delete_not_logged_in(self):
        """ test delete view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tag/' + str(tag_1.tag_id) + '/delete/', safe='')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/delete/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tag_delete_logged_in(self):
        """ test delete view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/delete/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tag_delete_template(self):
        """ test delete view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/delete/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/tag/tag_delete.html')

    def test_tag_delete_get_user_context(self):
        """ test delete view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/delete/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_tag')

    def test_tag_delete_redirect(self):
        """ test delete view """

        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # login testuser
        login = self.client.login(username='testuser_tag', password='QVe1EH1Z5MshOW2GHS4b')
        # create url
        destination = urllib.parse.quote('/tag/' + str(tag_1.tag_id) + '/delete/', safe='/')
        # get response
        response = self.client.get('/tag/' + str(tag_1.tag_id) + '/delete', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
