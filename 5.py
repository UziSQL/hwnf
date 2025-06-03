from typing import List, Any, Dict, Set, Generator

def squares_gen(n: int) -> Generator[int, None, None]:
    return (i * i for i in range(n))

print(list(squares_gen(5)))