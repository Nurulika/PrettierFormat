# test_prettierformat.py
"""
Tests for PrettierFormat module.
"""

import unittest
from prettierformat import PrettierFormat

class TestPrettierFormat(unittest.TestCase):
    """Test cases for PrettierFormat class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrettierFormat()
        self.assertIsInstance(instance, PrettierFormat)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrettierFormat()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
