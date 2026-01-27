'''adj = defaultdict(list)
    # Standard edges: u -> v (cost w)
    # Reversed edges: u -> v (cost 2w)
    for u, v, w in edges:
        adj[u].append((v, w))
        # This represents arriving at V and flipping the edge to go back to U
        adj[v].append((u, 2 * w))

    # Standard Dijkstra
    pq = [(0, 0)]  # (cost, current_node)
    dist = {i: float('inf') for i in range(n)}
    dist[0] = 0
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        if u == n - 1:
            return d
            
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
                
    return -1 if dist[n-1] == float('inf') else dist[n-1]'''
class Solution(object):
    def minCost(self, n, edges):
        heap = [(0, 0)]
        visited = {0}
        graph = defaultdict(set)

        for x, y, w in edges:
            graph[x].add((w, y))
            graph[y].add((2*w, x))
        while heap:
            weight, cur = heapq.heappop(heap)
            visited.add(cur)
            if cur == n - 1:
                return weight
            for nWeight, neigh in graph[cur]:
                if neigh not in visited:
                    heapq.heappush(heap, (weight+nWeight, neigh))
        return -1

        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        