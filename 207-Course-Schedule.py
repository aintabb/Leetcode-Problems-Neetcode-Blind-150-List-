"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""


# Time Complexity:  O(V+E)
# Space Complexity: O(V)

import collections
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        num_courses, prerequisites = 2, [[1, 0]]

        result = self.can_finish(num_courses, prerequisites)
        assert result == True, err_msg_invalid_result
        print(result)

        num_courses, prerequisites = 2, [[1,0], [0,1]]

        result = self.can_finish(num_courses, prerequisites)
        assert result == False, err_msg_invalid_result
        print(result)


    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        graph_map = collections.defaultdict(list)

        for node, edge in prerequisites:
            graph_map[node].append(edge)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * num_courses

        def dfs(node: int) -> bool:
            state = states[node]

            if (state == VISITED):
                return True
            if (state == VISITING):
                return False

            states[node] = VISITING
            for neighbor in graph_map[node]:
                if not dfs(neighbor):
                    return False

            states[node] = VISITED
            return True

        for i in range(num_courses):
            if not dfs(i):
                return False

        return True



# Create an instance of the class
solution = Solution()