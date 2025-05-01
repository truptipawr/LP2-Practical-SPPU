from collections import deque

# Function to find the minimum operations to obtain
# d liters in one jug
#Given two empty jugs of m and n litres respectively. The jugs don’t have markings to allow measuring smaller quantities. You have to use the jugs to measure d litres of water. The task is to find the minimum number of operations to be performed to obtain d litres of water in one of the jugs. In case of no solution exist, return -1.
def min_steps(m, n, d):
    if d > max(m, n):
        return -1 

    # Queue for BFS: (jug1, jug2, steps)
    q = deque([(0, 0, 0)])
    
    # For tracking the visited states
    visited = [[False] * (n + 1) for _ in range(m + 1)]  
    visited[0][0] = True

    while q:
        jug1, jug2, steps = q.popleft()

        if jug1 == d or jug2 == d:
            return steps

        # 1: Fill jug1
        if not visited[m][jug2]:
            visited[m][jug2] = True
            q.append((m, jug2, steps + 1))

        # 2: Fill jug2
        if not visited[jug1][n]:
            visited[jug1][n] = True
            q.append((jug1, n, steps + 1))

        # 3: Empty jug1
        if not visited[0][jug2]:
            visited[0][jug2] = True
            q.append((0, jug2, steps + 1))

        # 4: Empty jug2
        if not visited[jug1][0]:
            visited[jug1][0] = True
            q.append((jug1, 0, steps + 1))

        # 5: Pour jug1 into jug2
        pour1to2 = min(jug1, n - jug2)
        if not visited[jug1 - pour1to2][jug2 + pour1to2]:
            visited[jug1 - pour1to2][jug2 + pour1to2] = True
            q.append((jug1 - pour1to2, jug2 + pour1to2, steps + 1))

        # 6: Pour jug2 into jug1
        pour2to1 = min(jug2, m - jug1)
        if not visited[jug1 + pour2to1][jug2 - pour2to1]:
            visited[jug1 + pour2to1][jug2 - pour2to1] = True
            q.append((jug1 + pour2to1, jug2 - pour2to1, steps + 1))

    return -1  

if __name__ == "__main__":
  
    # jug1 = 4 litre, jug2 = 3 litre 
    m, n, d = 4, 3, 2
    print(min_steps(m, n, d))
