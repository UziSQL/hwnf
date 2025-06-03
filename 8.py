from typing import List, Any, Dict, Set, Generator

def unique_values(nested_list: List[List[Any]]) -> Set[Any]:
    return {item for sublist in nested_list for item in sublist}

print(unique_values([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))