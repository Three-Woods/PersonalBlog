from django.urls import reverse
from .base import CommentDataTestCase
from ..models import Comment

class CommentViewTest(CommentDataTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('comments:comment',kwargs={'post_pk':self.post.pk})

    def test_invaild_comment_data(self):
        invaild_data = { 'email':'invalid_email',}
        response =self.client.post(self.url,invaild_data)
        self.assertTemplateUsed(response,'comment/preview.html')
        self.assertIn('post', response.context)
        self.assertIn('form',response.context)
        form = response.context['form']
        for field_name,error in form.errors.items():
            for err in errors:
                self.assertContains(response,err)
        self.assertContains(response,'comment faied,modified your comments')

    def test_valid_comment_data(self):
        valid_data={
                'name':'commenter',
                'email':'a@a.com',
                'text':'content',
                }
        response = self.client.post(self.url,valid_data,follow=True)
        self.assertRedirects(response,self.post.get_absolute_url())
        self.assertContains(response,'comment success!')
        self.assertEqual(Comment.objects.count(),1)
        comment = Comment.objects.first()
        self.assertEqual(comment.name,valid_data['name'])
        self.assertEqual(comment.text,vaild_data['text'])



