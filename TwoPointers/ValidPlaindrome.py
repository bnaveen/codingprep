import unittest
import time
import statistics
from memory_profiler import memory_usage
from typing import Any, Callable, List, Tuple

from leetcode_tester import LeetCodeTester

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))

    def test_invalid_palindrome(self):
        self.assertFalse(self.solution.isPalindrome("race a car"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isPalindrome(""))

    def test_single_character(self):
        self.assertTrue(self.solution.isPalindrome("a"))

    def test_numeric_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("12321"))

    def test_mixed_case_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("Able was I ere I saw Elba"))



def run_unit_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    unittest.TextTestRunner(verbosity=2).run(suite)

def run_performance_tests():
    tester = LeetCodeTester(Solution)
    
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("abcdefghijklmnopqrstuvwxyz" * 1000, False)  # Large input to stress test
    ]
    
    tester.test_function("isPalindrome", test_cases, runs=10)

if __name__ == '__main__':
    print("Running unit tests:")
    run_unit_tests()
    
    print("\nRunning performance tests:")
    run_performance_tests()