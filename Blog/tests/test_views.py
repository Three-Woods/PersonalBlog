from django.apps import apps
from django.test import TestCase
from Blog.models import Post, Category, Tag
from django.contrib.auth.models import User
from django.utils import timezone
from  datetime import timedelta
from django.urls import reverse
#from datetime import *
class BlogDataTestCase(TestCase):
    def setUp(self):
       # apps.get_app_config('haystack').signal_processor.teardown()

        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@hellomin.com',
            password='admin', )

        self.cate1 = Category.objects.create(name='test_category1')
        self.cate2 = Category.objects.create(name='test_category2')
        
        self.tag1 = Tag.objects.create(name='test tag1')
        self.tag2 = Tag.objects.create(name='test tag2')

        self.post1=Post.objects.create(
            title='test_title1',
            body='test_context',
            category=self.cate1,
            author=self.user,)

        self.post1.tag.add(self.tag1)
        self.post1.save()

        self.post2 = Post.objects.create(
            title='test_title2',
            body='test_context2',
            category =self.cate2,
            author=self.user,
            create_time = timezone.now() -timedelta(days=100),
                )


class CategoryViewTestCase(BlogDataTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('blog:category',kwargs={'pk':self.cate1.pk})
        self.url2 = reverse('blog:category',kwargs={'pk':self.cate2.pk})

    def test_visit_a_nonexistent_category(self):
        url = reverse('blog:category',kwargs={'pk':100})
        response =self.client.get(url)
        self.assertEqual(response.status_code,404)

    def test_without_any_post(self):
        Post.objects.all().delete()
        response =self.client.get(self.url2)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('blog/index.html')
        self.assertContains(response,'no posts')
    
    def test_with_posts(self):
        response =self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.post1.title)
        self.assertIn('post_list',response.context)
        self.assertIn('is_paginated',response.context)
        self.assertIn('page_obj',response.context)
        self.assertEqual(response.context['post_list'].count(),1)
        expected_qs = self.cate1.post_set.all().order_by('-create_time')
        self.assertQuerysetEqual(response.context['post_list'],[repr(p) for p in expected_qs])

class PostDetailViewTestCase(BlogDataTestCase):
    def setUp(self):
        super().setUp()
        self.md_post = Post.objects.create(
            title = 'Markdown title_test',
            body = '#title1',
            author = self.user,
            category = self.cate1,
                )

        self.url = reverse('blog:detail',kwargs={'pk':self.md_post.pk})

    def test_good_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('blog/detail.html')
        self.assertContains(response,self.md_post.title)
        self.assertIn('Post',response.context)

    def test_visit_a_nonexistent_post(self):
        url = reverse('blog:detail',kwargs={'pk':100})
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)
    
    def test_increase_views(self):
        self.client.get(self.url)
        self.md_post.refresh_from_db()
        self.assertEqual(self.md_post.views,1)
       
        self.client.get(self.url)
        self.md_post.refresh_from_db()
        self.assertEqual(self.md_post.views,2)

    def test_markdownify_post_body_and_set_toc(self):
        response = self.client.get(self.url)
        self.assertContains(response,'title_catelogue')
        self.assertContains(response,self.md_post.title)

        post_template_var = response.context['post']
        self.assertHTMLEqual(post_template_var.body_html,"<h1 id='title'>title</h1>")
        self.assertHTMLEqual(post_template_var.toc,'<li><a href="#title">title</li>')


class AdminTestCase(BlogDataTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('admin:blog_post_add')

    def test_set_author_after_pubulishing_the_post(self):
        data = {
            'title':'test title',
            'body':'test context',
            'category':self.cate1.pk,
                }
        self.client.login(username=self.user.username,password='admin')
        response = self.client.post(self.url,data=data)
        self.assertEqual(post.author,self.user)
        self.assertEqual(post.title,data.get('title'))
        self.assertEqual(post.category,self.cate1)

class RSSTestCase(BlogDataTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('rss')

    def test_rss_subscription_content(self):
        response = self.client.get(self.url)
        self.assertContains(response,AllPostsRssFeed.title)
        self.assertContains(response,AllPostsRssFeed.description)
        self.assertContains(response,self.post1.title)
        self.assertContains(response,self.post2.title)
        self.assertContains(response,'[%s]%s'%(self.post1.category,self.post1.title))
        self.assertContains(response,'[%s]%s'%(self.post2.category,self.post2.title))
        self.assertContains(response,self.post2.body)
        self.assertContains(response,self.post2.body)
        




