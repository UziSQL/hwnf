from typing import List, Any, Dict, Set, Generator

def common_elements(lists: List[List[Any]]) -> Set[Any]:
    return {x for x in lists[0] if all(x in sublist for sublist in lists[1:])} if lists else set()

print(common_elements([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))