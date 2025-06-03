from typing import List, Any, Dict, Set, Generator

def list_to_dict(lst: List[Any]) -> Dict[int, Any]:
    return {i: v for i, v in enumerate(lst)}

print(list_to_dict(['a', 'b', 'c']))