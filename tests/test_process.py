import unittest
import pandas as pd
import os
import sys

# Add repo root to sys.path so 'src' is found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.process_sales import process_sales_data

class TestProcessSales(unittest.TestCase):
    def test_process_sales_data(self):
        # Create a tiny temp CSV for testing
        test_data = """product,price,quantity
TestItem,100,10"""
        with open("temp_test.csv", "w") as f:
            f.write(test_data)
        
        # Run the function
        result = process_sales_data("temp_test.csv", "temp_summary.csv")
        
        # Assertions
        self.assertEqual(result["Total Revenue"][0], 1000)
        self.assertEqual(result["Total Rows Processed"][0], 1)
        
        # Cleanup
        os.remove("temp_test.csv")
        os.remove("temp_summary.csv")

if __name__ == "__main__":
    unittest.main()
