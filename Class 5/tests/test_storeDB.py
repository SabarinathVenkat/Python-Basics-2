import unittest

from class5.store.dbutils import storeDB


class TestDefaultStoreDB(unittest.TestCase):

    def setUp(self):
        self.db = storeDB()

    def test_default_storeDB(self):
        self.assertEquals(self.db.dbname, 'default', "DB Name not set to default")

    def test_table_list(self):
        self.assertEquals(self.db.get_table_list(), {'products','sales'}, "Required tables are not created")

    def test_isTableEmpty(self):
        self.assertFalse(self.db.isTableEmpty('products'),"Product is Empty")

    def test_getProductCount(self):
        self.assertEquals(self.db.get_table_count('products'),3)

    def test_getSalesCount(self):
        self.assertEqual(self.db.get_table_count('sales'),0)

    def tearDown(self):
        del self.db

if __name__ == '__main__':
    unittest.main()