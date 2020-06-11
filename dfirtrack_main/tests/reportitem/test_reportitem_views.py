from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.models import Headline, Reportitem, System, Systemstatus
import urllib.parse

class ReportitemViewTestCase(TestCase):
    """ reportitem view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        headline_1 = Headline.objects.create(headline_name='headline_1')

        # create object
        Reportitem.objects.create(
            reportitem_note='lorem ipsum',
            system = system_1,
            headline = headline_1,
            reportitem_created_by_user_id = test_user,
            reportitem_modified_by_user_id = test_user,
        )

    def test_reportitem_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitem/', safe='')
        # get response
        response = self.client.get('/reportitem/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitem_list.html')

    def test_reportitem_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

    def test_reportitem_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # create url
        destination = urllib.parse.quote('/reportitem/', safe='/')
        # get response
        response = self.client.get('/reportitem', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_reportitem_detail_not_logged_in(self):
        """ test detail view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitem/' + str(reportitem_1.reportitem_id) + '/', safe='')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_detail_logged_in(self):
        """ test detail view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_detail_template(self):
        """ test detail view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitem_detail.html')

    def test_reportitem_detail_get_user_context(self):
        """ test detail view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

    def test_reportitem_detail_redirect(self):
        """ test detail view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # create url
        destination = urllib.parse.quote('/reportitem/' + str(reportitem_1.reportitem_id) + '/', safe='/')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_reportitem_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitem/add/', safe='')
        # get response
        response = self.client.get('/reportitem/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitem_add.html')

    def test_reportitem_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

    def test_reportitem_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # create url
        destination = urllib.parse.quote('/reportitem/add/', safe='/')
        # get response
        response = self.client.get('/reportitem/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_reportitem_edit_not_logged_in(self):
        """ test edit view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_edit_logged_in(self):
        """ test edit view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_edit_template(self):
        """ test edit view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitem_edit.html')

    def test_reportitem_edit_get_user_context(self):
        """ test edit view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

    def test_reportitem_edit_redirect(self):
        """ test edit view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # create url
        destination = urllib.parse.quote('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
