# a = 10

# if (a > 20):
#     b = True
# else:
#     b = False
    
# print(b)

''''''

# weekday 라는 변수의 값이 0이면 일요일 1이면 월요일 6이면 토요일을 저장하고자 하는 경우
#dict로 해결
# switcher = {
#     0: "일요일", 1: "월요일", 2: "화요일", 3: "수요일", 4: "목요일",
#     5: "금요일", 6: "토요일"
# }

# weekday = 4

# print(switcher.get(weekday, "없을 때 값"))

''''''

# weekday = 2
# match weekday:
#     case 0:
#         print("일요일")
#     case 0:
#         print("월요일")
#     case 0:
#         print("화요일")
#     case 0:
#         print("수요일")
#     case 0:
#         print("목요일")
#     case 0:
#         print("금요일")
#     case 0:
#         print("토요일")
#     case _:
#         print("요일 없음")

''''''

# var = 1
# while var < 4:
#     print("exel", var)
#     var = var + 1


''''''

# for i in range(5):
#     for j in range(5):
#         print("{0}". format('*'), end="")
#     print()

''''''


# MAX = 100
# def main():
#     isPrime = [1] * (MAX + 1)
#     isPrime[0] = 0; isPrime[1] = 0
#     for i in range(2, int(MAX ** 0.5) + 1):
#         if (isPrime[i]):
#             for j in range(i * i, MAX + 1, i):
#                 isPrime[j] = 0
    
#     for i in range(MAX):
#         if (isPrime[i]):
#             print(i)

# main()

''''''

# 간단한 예제
#1
# ans = 0
# li = []
# def fc(num):
#     global ans
#     temp = 0
#     for i in range(1, int(num / 2) + 1):
#         if (num % i == 0):
#             temp += i
    
#     if (temp == num):
#         ans += 1
#         li.append(num)

# def main():
#     for i in range(2, 1001):
#         fc(i)
#     print(ans)
#     print(li)

# main()


#2 윤년 구하기

# ans = 0
# def fc(year):
#     global ans
#     if (year % 4 == 0 and year % 100 != 0):
#         ans += 1
#     if (year % 400 == 0):
#         ans += 1

# def main():
#     for i in range(1, 2027):
#         fc(i)
#     print(ans)

# main()


#3 피보나치

# def main():
#     li = [1, 1]
#     for i in range(2, 20):
#         li.append(li[i - 2] + li[i - 1])

#     print(li)

# main()


#4 BFS 기본형 (그래프 인접 리스트)

# from collections import deque

# graph = {
#     1: [2, 3],
#     2: [1, 4],
#     3: [1, 4],
#     4: [2, 3, 5],
#     5: [4]
# }

# def bfs(graph, start):
#     visited = [start]
#     # queue = deque([start])
#     queue = deque()
#     queue.append(start)

#     while queue:
#         node = queue.popleft()
#         print(node, end=" ")
#         for next_node in graph[node]:
#             if next_node not in visited:
#                 visited.append(next_node)
#                 queue.append(next_node)

# bfs(graph, 1)


#5 다익스트라 (우선순위 큐)

# import heapq

# graph2 = {
#     1: [(2, 2), (3, 5)],   # (다음노드, 가중치)
#     2: [(1, 2), (3, 1), (4, 3)],
#     3: [(1, 5), (2, 1), (4, 1)],
#     4: [(2, 3), (3, 1)]
# }

# INF = int(1e9)

# def dijkstra(graph, start):
#     distance = {node: INF for node in graph}
#     distance[start] = 0
#     queue = [(0, start)]  # (거리, 노드)

#     while queue:
#         dist, node = heapq.heappop(queue)

#         if dist > distance[node]:
#             continue

#         for next_node, weight in graph[node]:
#             new_dist = dist + weight
#             if new_dist < distance[next_node]:
#                 distance[next_node] = new_dist
#                 heapq.heappush(queue, (new_dist, next_node))

#     return distance

# print(dijkstra(graph2, 1))


# print(dir(__builtins__))


''''''


