import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
def test_get_ts(self):
    import time
    t=time.time()
    ts=str(int(round(t*1000)))
    print(ts)
self.assertEqual(True, get_ts())

if __name__ == '__main__':
    unittest.main()
