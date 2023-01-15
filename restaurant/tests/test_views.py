from django.test import TestCase
from restaurant import models
from restaurant.serializer import MenuSeralizer

class MenuViewTest(TestCase):
  def setUp(self):
    models.Menu.objects.create(id=1,title="IceCream", price=80, inventory=100)
    models.Menu.objects.create(id=2,title="Cake", price=1, inventory=13)
    models.Menu.objects.create(id=3,title="Soda", price=10, inventory=2)

  def test_get__all(self):
    items = models.Menu.objects.all()
    items_serialized = MenuSeralizer(data=items, many=True)
    items_serialized.is_valid()

    items_created = [
      {
      'id':1,
      'title':"IceCream", 
      'price':'80', 
      'inventory':100
      },{
      'id':2,
      'title':"Cake", 
      'price':'1', 
      'inventory':13
      },
      {
      'id':3,
      'title':"Soda", 
      'price':'10', 
      'inventory':2
      }
    ]

    correct_serialized = MenuSeralizer(data=items_created,many=True)
    correct_serialized.is_valid()


    self.assertQuerysetEqual(items_serialized.data, correct_serialized.data)