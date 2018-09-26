import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        """
            测试是否大小写一致
        """
        self.assertEqual('foo'.upper(), 'CC')

    def test_isupper(self):
        """
            测试是否全部大写
        """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """
            测试是否分割正确
        """
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
    
    
    