import unittest
import lcdmusic

class EnsureTestOutput(unittest.TestCase):
    def test(self):
        outputFile = open("testFile.txt", "rb")
        self.assertAreEqual(outputFile, "test")
