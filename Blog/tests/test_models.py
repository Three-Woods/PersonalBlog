from django.apps import apps
from django.test import TestCase
from Blog.models import Post, Category, Tag
from django.contrib.auth.models import User
from django.urls import reverse

class PostModelTestCase(TestCase):
    def setUp(self):
 #       apps.get_app_config('haystack').signal_processor.teardown()
        user = User.objects.create_superuser(
            username = 'admin',
            email = 'admin@hellogithub.com',
            password='admin', )
        cate = Category.objects.create(name='test1')
        self.post = Post.objects.create(
            title = 'test title',
            body = 'test context',
            category = cate,
            author =user,
                )


    def test_str_representation(self):
        self.assertEqual(self.post.__str__(),self.post.title)
    
    def test_auto_populate_modified_time(self):
        self.assertIsNotNone(self.post.modified_time)

        old_post_modified_time =self.post.modified_time
        self.post.body='new test_context'
        self.post.save()
        self.post.refresh_from_db()
        self.assertTrue(self.post.modified_time>old_post_modified_time)

    def test_get_absolute_url(self):
        expected_url =reverse('blog:detail',kwargs={'pk':self.post.pk})
        self.assertEqual(self.post.get_absolute_url(),expected_url)

    def test_increase_views(self):
        self.post.increase_views()
        self.post.refresh_from_db()
        self.assertEqual(self.post.views,1)

        self.post.increase_views()
        self.post.refresh_from_db()
        self.assertEqual(self.post.views,2)



