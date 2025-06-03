from typing import List, Any, Dict, Set, Generator

def flatten(nested_list: List[List[Any]]) -> List[Any]:
    return [item for sublist in nested_list for item in sublist]

print(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))