from django.apps import apps
from django.contrib.auth.models import User
from django.test import TestCase

from Blog.models import Category, Post

class CommentDataTestCase(TestCase):
    def setUp(self):
#        apps.get_app_config('haystack').signal_processor.teardown()
        self.user = User.objects.create_superuser(
                username='admin',
                email='admin@hellogithub.com',
                password='admin',
                )

        self.cate = Category.objects.create(name='test')
        self.post= Post.objects.create(
                title='test_title',
                body='test_context',
                category=self.cate,
                author=self.user,
                )

