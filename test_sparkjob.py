# test_sparkjob.py
"""
Tests for SparkJob module.
"""

import unittest
from sparkjob import SparkJob

class TestSparkJob(unittest.TestCase):
    """Test cases for SparkJob class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SparkJob()
        self.assertIsInstance(instance, SparkJob)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SparkJob()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
