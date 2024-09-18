import unittest
from src.data_loader import load_dealers

class TestDataLoader(unittest.TestCase):
    def test_load_dealers(self):
        dealers = load_dealers('data/dealers.csv')
        self.assertEqual(len(dealers), 3)
        self.assertEqual(dealers[0].name, "MetalCorp")

if __name__ == '__main__':
    unittest.main()
