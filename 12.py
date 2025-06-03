from typing import List, Any, Dict, Set, Generator

def intersection(sets: List[Set[Any]]) -> Set[Any]:
    return {x for x in sets[0] if all(x in s for s in sets[1:])} if sets else set()

print(intersection([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]))
