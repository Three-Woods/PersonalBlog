import os
import pathlib
import random
import sys
from datetime import timedelta
import django
import faker
from django.utils import timezone
#from django.conf import settings
#os.environ.setdefault("DJNAGO_SETTINGS_MODULE", "Web_app.settings")
#django.setup()

back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print('hi')
print(back)
print(__file__)
print(BASE_DIR)
if __name__=='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web_app.settings")
    django.setup()
    from Blog.models import Category,Post,Tag
    from comments.models import Comment
    from django.contrib.auth.models import User
   # settings.configure(default_settings=Web_app_defaults,DEBUG=True)
   # os.environ['DJNAGO_SETTINGS_MODULE']= 'Web_app.settings'
   # django.setup()
    print('hi')
    print('clean database')
    Post.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()
    Comment.objects.all().delete()
    User.objects.all().delete()

    print('Create a blog user')
    user =User.objects.create_superuser('admin@hellogithub.com','admin')
    category_list = ['python study','Opensource','tool resource','life','test']
    tag_list = ['django','Python','pipenv','Docker','Nginx','Elasticsearch','Supervisor']
    a_year_ago = timezone.now()-timedelta(days=365)

    print('create categries and tags')
    for cate in category_list:
        Category.objects.create(name=cate)

    for tag in tag_list:
        Tag.objects.create(name=tag)

    print('Create a markdown sample post')
    Post.objects.create(
            title='Markdown and Codehighlight test',
            body = pathlib.Path(BASE_DIR).joinpath('scripts','md.sample').read_text(encoding='utf-8'),
            category=Category.objects.create(name='Markdown'),
            author = user,
            )

    print('create some faked posts published within the past year')
    fake = faker.Faker()
    for _ in range(100):
        tags = Tag.objects.order_by('?')
        tag1 = tags.first()
        tag2 = tags.last()
        cate = Category.objects.order_by('?').first()
        create_time =   fake.date_time_between(start_date='-1y',end_date="now",tzinfo=timezone.get_current_timezone())
        post = Post.objects.create(
              title = fake.sentence().rstrip('.'),
              body='\n\n'.join(fake.paragraphs(10)),
              create_time=create_time,
              category=cate,
              author=user,
              
                )
        post.tag.add(tag1,tag2)
        post.save()

    print('create some faked posts published within the past year')
    fake = faker.Faker('zh_CN')
    for _ in range(100):
        tags = Tag.objects.order_by('?')
        tag1 = tags.first()
        tag2 = tags.last()
        cate = Category.objects.order_by('?').first()
        create_time = fake.date_time_between(start_date='-1y',end_date="now",tzinfo=timezone.get_current_timezone())
        post = Post.objects.create(
              title = fake.sentence().rstrip('.'),
              body='\n\n'.join(fake.paragraphs(10)),
              create_time=create_time,
              category=cate,
              author=user,
                )
        post.tag.add(tag1,tag2)
        post.save()

    print('create some comments')

    for post in Post.objects.all()[:20]:
        post_create_time = post.create_time
        delta_in_days='-'+str((timezone.now()-post_create_time).days)+'d'
        for _ in range(random.randrange(3,15)):
            Comment.objects.create(
                    name=fake.name(),
                    email =fake.email(),
                    url=fake.uri(),
                    text = fake.paragraph(),
                    created_time=fake.date_time_between(
                        start_date=delta_in_days,
                        end_date="now",
                        tzinfo=timezone.get_current_timezone()),
                        post=post,
                    )
        print('done!')
