from django.test import TestCase

from weblogs.models import Blog, Author, Entry


class BlogTestCase(TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_new_blog_save(self):
    b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
    b.save()
    self.assertEquals(b.name, 'Beatles Blog')
    b.name = 'New name'
    self.assertEquals(b.name, 'New name')
