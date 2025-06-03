from typing import List, Any, Dict, Set, Generator

def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    return {v: k for k, v in d.items()}

print(invert_dict({'a': 1, 'b': 2, 'c': 3}))