from typing import List, Any, Dict, Set, Generator

def reverse_gen(lst: List[Any]) -> Generator[Any, None, None]:
    return (lst[i] for i in range(len(lst) - 1, -1, -1))

print(list(reverse_gen([1, 2, 3, 4, 5])))