import time
import statistics
from memory_profiler import memory_usage
import matplotlib.pyplot as plt
from typing import Any, Callable, List, Tuple

class LeetCodeTester:
    def __init__(self, solution_class: type):
        self.solution = solution_class()

    def test_function(self, func_name: str, test_cases: List[Tuple[Any, Any]], runs: int = 5):
        func = getattr(self.solution, func_name)
        
        print(f"Testing function: {func_name}")
        
        all_times = []
        all_memories = []
        
        for i, (inputs, expected) in enumerate(test_cases, 1):
            print(f"\nTest Case {i}:")
            print(f"Input: {inputs}")
            print(f"Expected Output: {expected}")
            
            times = []
            memories = []
            
            for _ in range(runs):
                start_time = time.perf_counter()
                if isinstance(inputs, tuple):
                    result = func(*inputs)
                else:
                    result = func(inputs)
                end_time = time.perf_counter()
                
                execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
                times.append(execution_time)
                
                mem_usage = max(memory_usage((func, inputs if isinstance(inputs, tuple) else (inputs,)), max_iterations=1))
                memories.append(mem_usage)
            
            all_times.extend(times)
            all_memories.extend(memories)
            
            best_time = min(times)
            avg_time = statistics.mean(times)
            best_memory = min(memories)
            avg_memory = statistics.mean(memories)
            
            print(f"Actual Output: {result}")
            print(f"Correct: {result == expected}")
            print(f"Best Time: {best_time:.2f} ms")
            print(f"Average Time: {avg_time:.2f} ms")
            print(f"Best Memory: {best_memory:.2f} MiB")
            print(f"Average Memory: {avg_memory:.2f} MiB")
        
        self.plot_results(all_times, all_memories)

    def plot_results(self, times, memories):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
        
        ax1.plot(times, label='Execution Time')
        ax1.set_title('Execution Time per Run')
        ax1.set_xlabel('Run')
        ax1.set_ylabel('Time (ms)')
        ax1.legend()
        
        ax2.plot(memories, label='Memory Usage', color='red')
        ax2.set_title('Memory Usage per Run')
        ax2.set_xlabel('Run')
        ax2.set_ylabel('Memory (MiB)')
        ax2.legend()
        
        plt.tight_layout()
        plt.savefig('performance_results.png')
        print("Performance graph saved as 'performance_results.png'")

# Usage remains the same
if __name__ == '__main__':
    class Solution:
        def isPalindrome(self, s: str) -> bool:
            newStr = ""
            for c in s:
                if c.isalnum():
                    newStr += c.lower()
            return newStr == newStr[::-1]

    tester = LeetCodeTester(Solution)
    
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("abcdefghijklmnopqrstuvwxyz" * 1000, False)  # Large input to stress test
    ]
    
    tester.test_function("isPalindrome", test_cases, runs=10)