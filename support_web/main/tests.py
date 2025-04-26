from django.test import TestCase
from .models import Issues
from .models import Moderators

class IssuesTestCase(TestCase):
    def test_issue_creation(self):
        issue = Issues.objects.create(full_name='John Doe', issue='Test issue', issue_description='This is a test issue')
        self.assertEqual(issue.full_name, 'John Doe')
        self.assertEqual(issue.issue, 'Test issue')
        self.assertEqual(issue.issue_description, 'This is a test issue')
        
        
        
        
class ModeratorsTestCase(TestCase):
    def test_moderator_creation(self):
        moderator = Moderators.objects.create(full_name='Иван', mail = "test@mail.ru")
        self.assertEqual(moderator.full_name, 'Иван')
        self.assertEqual(moderator.mail, 'test@mail.ru')
        
        
        
    