from .base import CommentDataTestCase
from ..models import Comment

class CommentModelTestCase(CommentDataTestCase):
    def setUp(self):
        super().setUp()
        self.comment = Comment.objects.create(
            name='username',
            email='admin@sad.com',
            text='comment content',
            post = self.post,
                )


    def test_str_representation(self):
        self.assertEqual(self.comment.__str__(),'commenter:content')
