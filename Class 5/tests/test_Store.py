import unittest

from class5.store.store import Store

class TestStore(unittest.TestCase):

    def setUp(self):
        self.store = Store("TestStore")

   # def test_sell(self):
   #     self.store.sell(1,20)
    #    self.assertEqual(self.store.get_prod_left(1),80)

    def test_returns(self):
        self.store.return_product(1,20)
        self.assertEqual(self.store.get_prod_left(1),120)

    def tearDown(self):
        del self.store

if __name__ == '__main__':
    unittest.main()