from typing import List, Any, Dict, Set, Generator
from math import factorial

def factorials_gen(n: int) -> Generator[int, None, None]:
    return (factorial(i) for i in range(1, n + 1))

print(list(factorials_gen(5)))