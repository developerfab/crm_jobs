# -*- coding: utf-8 -*-
from django.test import TestCase
from models import ContactUser


class ContactTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_contact_case_developer(self):
        """Create a contact case for developer"""
        developer = ContactUser.objects.create(name="Gustavo Angulo", kind=0)
        self.assertEqual(developer.name, 'Gustavo Angulo')
        self.assertEqual(developer.type, 0)

    def test_create_contact_developer_all_fields(self):
        """Create a contact case for developer with all fields"""
        developer = ContactUser.objects.create(name="Gustavo Angulo", kind=0, email="woakas@gmail.com", tel="3002141910")
        self.assertEqual(developer.tel, '3002141910')

    def test_tel_field(self):
        """Create a contact case for developer"""
        developer = ContactUser.objects.create(name="Gustavo Angulo", kind=0, tel="+3002141910")
        self.assertEqual(developer.name, 'Gustavo Angulo')
        self.assertEqual(developer.tel, '+3002141910')
