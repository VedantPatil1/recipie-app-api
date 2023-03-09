"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_sucessful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'test_password123'
        user = get_user_model().objects.create_user(
            email=password,
            password=password,
        )
        
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
