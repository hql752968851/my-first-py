import unittest
from post_yaodao import *
import random
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
def test_get_ts(self):
    import time
    t=time.time()
    ts=str(int(round(t*1000)))
    print(ts)
    get_ts=mock.Mock(return_value='1584686878805')
    self.assertEqual('1584686878805', get_ts())


def test_get_salt(self):
    s=str(random.randint(0, 10))
    t=get_ts()
    return t+s



self.assertEqual(True, get_ts())

def test_get_salt(self);

if __name__ == '__main__':
    unittest.main()
12223