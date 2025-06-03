from typing import List, Any, Dict, Set, Generator

def char_counts(text: str) -> Dict[str, int]:
    res = {}
    for char in text:
        if char not in res:
            res[char] = text.count(char)
    return res

print(char_counts("hello"))