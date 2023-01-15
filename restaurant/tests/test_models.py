from django.test import TestCase
from restaurant import models

class MenuTest(TestCase):
  def test_get_item(self):
    item = models.Menu.objects.create(id=1,title="IceCream", price=80, inventory=100)
    self.assertEqual(item.__str__(), "IceCream : 80")
