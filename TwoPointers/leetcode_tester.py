import time
import statistics
from memory_profiler import memory_usage
from typing import Any, Callable, List, Tuple

class LeetCodeTester:
    def __init__(self, solution_class: type):
        self.solution = solution_class()

    def test_function(self, func_name: str, test_cases: List[Tuple[Any, Any]], runs: int = 5):
        func = getattr(self.solution, func_name)
        
        print(f"Testing function: {func_name}")
        
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
                
                mem_usage = memory_usage((func, inputs if isinstance(inputs, tuple) else (inputs,)), max_iterations=1)
                memories.append(max(mem_usage))
            
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