from typing import List, Any, Dict, Set, Generator

def unique_squares(numbers: List[int]) -> Set[int]:
    return {x * x for x in set(numbers)}

print(unique_squares([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))