#! /usr/bin/env python3
import unittest
import sys
from io import StringIO
from os.path import join, dirname
class TestEx03(unittest.TestCase):
    def setUp(self) :
        from os.path import exists
        if not exists(join(dirname(__file__),"dna.py")):
                        self.skipTest("no dna.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
        sys.modules.pop('dna')
    def test_small_1(self):
        sys.stdin = StringIO(f'databases/small.csv\nsequences/1.txt')
        import dna
        sys.stdout.seek(0)
        s = "Bob\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_small_2(self):
        sys.stdin = StringIO(f'databases/small.csv\nsequences/2.txt')
        import dna
        sys.stdout.seek(0)
        s = "No match\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_small_3(self):
        sys.stdin = StringIO(f'databases/small.csv\nsequences/3.txt')
        import dna
        sys.stdout.seek(0)
        s = "No match\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_small_4(self):
        sys.stdin = StringIO(f'databases/small.csv\nsequences/4.txt')
        import dna
        sys.stdout.seek(0)
        s = "Alice\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_5(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/5.txt')
        import dna
        sys.stdout.seek(0)
        s = "Lavender\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_6(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/6.txt')
        import dna
        sys.stdout.seek(0)
        s = "Luna\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_7(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/7.txt')
        import dna
        sys.stdout.seek(0)
        s = "Ron\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_8(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/8.txt')
        import dna
        sys.stdout.seek(0)
        s = "Ginny\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_9(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/9.txt')
        import dna
        sys.stdout.seek(0)
        s = "Draco\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_10(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/10.txt')
        import dna
        sys.stdout.seek(0)
        s = "Albus\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_11(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/11.txt')
        import dna
        sys.stdout.seek(0)
        s = "Hermione\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_12(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/12.txt')
        import dna
        sys.stdout.seek(0)
        s = "Lily\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_13(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/13.txt')
        import dna
        sys.stdout.seek(0)
        s = "No match\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_14(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/14.txt')
        import dna
        sys.stdout.seek(0)
        s = "Severus\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_15(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/15.txt')
        import dna
        sys.stdout.seek(0)
        s = "Sirius\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_16(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/16.txt')
        import dna
        sys.stdout.seek(0)
        s = "No match\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_17(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/17.txt')
        import dna
        sys.stdout.seek(0)
        s = "Harry\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_18(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/18.txt')
        import dna
        sys.stdout.seek(0)
        s = "No match\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_19(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/19.txt')
        import dna
        sys.stdout.seek(0)
        s = "Fred\n"
        self.assertEqual(sys.stdout.read(), s)
    def test_large_20(self):
        sys.stdin = StringIO(f'databases/large.csv\nsequences/20.txt')
        import dna
        sys.stdout.seek(0)
        s = "No match\n"
        self.assertEqual(sys.stdout.read(), s)

unittest.main()