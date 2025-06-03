from typing import List, Any, Dict, Set, Generator

def primes_gen(n: int) -> Generator[int, None, None]:
    return (x for x in range(2, n + 1) if all(x % d != 0 for d in range(2, int(x ** 0.5) + 1)))

print(list(primes_gen(10)))