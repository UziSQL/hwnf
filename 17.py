from typing import List, Any, Dict, Set, Generator

def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    return {length: [word for word in words if len(word) == length] for length in {len(word) for word in words}}

print(group_by_length(['hello', 'world', 'python', 'is', 'fun']))
