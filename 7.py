from typing import List, Any, Dict, Set, Generator

def index_map(text: str) -> dict[str, int]:
    return {char: idx for idx, char in enumerate(text)}

print(print(index_map("hello")))