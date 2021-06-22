""" Invitation tests """

# Django
from django.test import TestCase

# Model
from cride.circles.models import Circle, Invitation
from cride.users.models import User


class InvitationManagerTestCase(TestCase):
    """ Invitations manager test case """

    def setUp(self):
        """ Test case setup """
        self.user = User.objects.create(
            first_name='Alexander',
            last_name='Sánchez',
            email='alexander@a.com',
            username='alexander',
            password='holamundo'
        )
        self.circle = Circle.objects.create(
            name='Facultad de Ciencias',
            slug_name='fciencias',
            about='Grupo oficial de la Facultad de Ciencias UTPL',
            verified=True
        )

    def test_code_generation(self):
        """ Random codes should be generated automatically """
        invitation = Invitation.objects.create(
            issued_by=self.user,
            circle=self.circle
        )
        self.assertIsNotNone(invitation.code)

    def test_code_usage(self):
        """ If a code is given, there's no need to create a new one """
        code = 'holamundo'
        invitation = Invitation.objects.create(
            issued_by=self.user,
            circle=self.circle,
            code=code
        )
        self.assertEqual(invitation.code, code)

    def test_code_generation_if_duplicated(self):
        """ If given code is not unique, a new one must be generated """
        code = Invitation.objects.create(
            issued_by=self.user,
            circle=self.circle
        ).code

        # Create another invitation with the past code
        invitation = Invitation.objects.create(
            issued_by=self.user,
            circle=self.circle,
            code=code
        )

        self.assertNotEqual(code, invitation.code)
