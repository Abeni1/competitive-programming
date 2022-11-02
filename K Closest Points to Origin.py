class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for x,y in points:
            heapq.heappush(heap,((math.sqrt(x**2 + y**2)),[x,y]))
        
        near_points = []
        n = 1
        while heap and n <= k:
            h = heapq.heappop(heap)
            near_points.append(h[1])
            n += 1
            
        return near_points
