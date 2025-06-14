from typing import List, Any, Dict, Set, Generator

def fibonacci_gen(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci_gen(10)))