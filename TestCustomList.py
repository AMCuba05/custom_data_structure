import unittest
from CustomList import CustomList

class TestCustomList(unittest.TestCase):
  
  def test_append_one_element(self):
      custom_list = CustomList(4)
      custom_list.append(1)
      self.assertEqual(custom_list.get_item(0) ,1)

  def test_pop_element(self):
      custom_list = CustomList(4)
      custom_list.append(1)
      custom_list.append(2)
      custom_list.append(3)
      custom_list.append(4)
      self.assertEqual(custom_list.pop() ,4)

  def test_replace_element_in_append(self):
      custom_list = CustomList(4)
      custom_list.append(1)
      custom_list.append(2)
      custom_list.append(3)
      custom_list.append(4)
      custom_list.append(5)
      self.assertEqual(custom_list.get_item(3) ,5)
      self.assertEqual(custom_list.get_item(0) ,2)
    
  def test_get_item(self):
      custom_list = CustomList(4)
      custom_list.append(1)
      custom_list.append(2)
      custom_list.append(3)
      custom_list.append(4)
      self.assertEqual(custom_list.get_item(3) ,4)

if __name__ == '__main__':
  unittest.main()
