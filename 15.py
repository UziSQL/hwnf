from typing import List, Any, Dict, Set, Generator

def transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))