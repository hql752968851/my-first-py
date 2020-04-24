import unittest
from post import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        import time
        t = time.time()
        ts = str(int(round(t * 1000)))
        print(ts)
        self.assertEqual('1584686878805',get_)
 def


if __name__ == '__main__':
    unittest.main()
