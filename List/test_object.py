import unittest
import object

class TestObject(unittest.TestCase):
	def test_add(self):
		l = object.UnorderedList()
		self.assertEqual(l.get_items(), [])
		l.add(3)
		self.assertEqual(l.get_items(), [3])
		l.add(5)
		self.assertEqual(l.get_items(), [5, 3])
		l.add(29)
		self.assertEqual(l.get_items(), [29, 5, 3])

	def test_append(self):
		l = object.UnorderedList()
		self.assertEqual(l.get_items(), [])
		l.append(5)
		self.assertEqual(l.get_items(), [5])
		l.append(3)
		self.assertEqual(l.get_items(), [5, 3])
		l.append(29)
		self.assertEqual(l.get_items(), [5, 3, 29])

	def test_insert(self):
		l = object.UnorderedList()
		self.assertEqual(l.get_items(), [])
		l.insert(0, 3)
		self.assertEqual(l.get_items(), [3])
		l.insert(1, 6)
		self.assertEqual(l.get_items(), [3, 6])
		l.insert(0, 7)
		self.assertEqual(l.get_items(), [7, 3, 6])
		l.insert(10, 9)
		self.assertEqual(l.get_items(), [7, 3, 6, 9])
		l.insert(2, 1)
		self.assertEqual(l.get_items(), [7, 3, 1, 6, 9])

	def test_remove(self):
		l = object.UnorderedList()
		l.add(3)
		l.remove(3)
		self.assertEqual(l.get_items(), [])
		l.add(5)
		l.append(7)
		l.insert(1, 2)
		l.append(9)
		l.add(6)
		l.remove(9)
		self.assertEqual(l.get_items(), [6, 5, 2, 7])
		l.remove(6)
		self.assertEqual(l.get_items(), [5, 2, 7])
		l.remove(2)
		self.assertEqual(l.get_items(), [5, 7])

	def test_pop(self):
		l = object.UnorderedList()
		l.add(3)
		c = l.pop()
		self.assertEqual(l.get_items(), [])
		self.assertEqual(c, 3)
		l.add(5)
		l.append(7)
		l.insert(1, 2)
		l.append(9)
		l.add(6)
		# [6, 5, 2, 7, 9]
		c = l.pop(0)
		self.assertEqual(l.get_items(), [5, 2, 7, 9])
		self.assertEqual(c, 6)
		c = l.pop()
		self.assertEqual(l.get_items(), [5, 2, 7])
		self.assertEqual(c, 9)
		c = l.pop(1)
		self.assertEqual(l.get_items(), [5, 7])
		self.assertEqual(c, 2)
		c = l.pop(1)
		self.assertEqual(l.get_items(), [5])
		self.assertEqual(c, 7)
		c = l.pop(0)
		self.assertEqual(l.get_items(), [])
		self.assertEqual(c, 5)

	def test_search(self):
		l = object.UnorderedList()
		self.assertEqual(l.search(1), False)
		l.add(5)
		l.append(7)
		l.insert(1, 2)
		l.append(9)
		l.add(6)
		# [6, 5, 2, 7, 9]
		self.assertEqual(l.search(6), True)
		self.assertEqual(l.search(9), True)
		self.assertEqual(l.search(2), True)
		self.assertEqual(l.search(8), False)

	def test_index(self):
		l = object.UnorderedList()
		l.add(5)
		self.assertEqual(l.index(5), 0)
		l.append(7)
		l.insert(1, 2)
		l.append(9)
		l.add(6)
		# [6, 5, 2, 7, 9]
		self.assertEqual(l.index(6), 0)
		self.assertEqual(l.index(5), 1)
		self.assertEqual(l.index(2), 2)
		self.assertEqual(l.index(7), 3)
		self.assertEqual(l.index(9), 4)
		
	def test_size(self):
		l = object.UnorderedList()
		self.assertEqual(l.size(), 0)
		l.add(5)
		l.pop()
		self.assertEqual(l.size(), 0)
		l.add(5)
		l.append(7)
		l.insert(1, 2)
		l.append(9)
		l.add(6)
		# [6, 5, 2, 7, 9]
		self.assertEqual(l.size(), 5)

	def test_isEmpty(self):
		l = object.UnorderedList()
		self.assertEqual(l.isEmpty(), True)
		l.add(5)
		self.assertEqual(l.isEmpty(), False)
		l.pop()
		self.assertEqual(l.isEmpty(), True)

	def test_ordered_add(self):
		l = object.OrderedList()
		self.assertEqual(l.get_items(), [])
		l.add(3)
		self.assertEqual(l.get_items(), [3])
		l.add(5)
		self.assertEqual(l.get_items(), [3, 5])
		l.add(1)
		self.assertEqual(l.get_items(), [1, 3, 5])
		l.add(9)
		self.assertEqual(l.get_items(), [1, 3, 5, 9])
		l.add(4)
		self.assertEqual(l.get_items(), [1, 3, 4, 5, 9])
		


		
