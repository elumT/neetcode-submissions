class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        ranks = [1] * n
        components = n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            nonlocal components

            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return
            
            if ranks[root_x] < ranks[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            ranks[root_x] += 1
            components -= 1

        for x,y in edges:
            union(x, y)
        
        return components
            



        