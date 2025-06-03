from typing import List, Any, Dict, Set, Generator

def str_lengths(strings: List[str]) -> Dict[str, int]:
    return {s: len(s) for s in strings}

print(str_lengths(['hello', 'world', 'python']))