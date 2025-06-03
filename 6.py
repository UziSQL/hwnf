from typing import List, Any, Dict, Set, Generator

def odd_squares(n: int) -> set[int]:
    return {i * i for i in range(n) if i % 2 == 1}

print(odd_squares(10))
