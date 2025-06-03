from typing import List, Any, Dict, Set, Generator

def squares(n: int) -> List[int]:
    return [i * i for i in range(n)]

print(squares(5))