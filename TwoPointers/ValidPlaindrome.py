import unittest

from leetcode_tester import LeetCodeTester

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

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