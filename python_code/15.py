"""
아래와 같은 2 × 2 격자의 왼쪽 위 모서리에서 출발하여 오른쪽 아래 모서리까지 도달하는 길은 모두 6가지가 있습니다 (거슬러 가지는 않기로 합니다).
그러면 20 × 20 격자에는 모두 몇 개의 경로가 있습니까?
"""


def f(n):
    line = [1] * n
    count = 0
    while True:
        for i, v in enumerate(line):
            if i is 0:
                line[i] += 1
            else:
                line[i] = line[i] + line[i - 1]
        yield line
        count += 1
        if count is n:
            break


gen = f(20)

res = 0
for line in gen:
    res = line[line.__len__() - 1]

print(res) # 137846528820

"""
다른 풀이
격자의 가로선을 a, 세로선을 b이면 좌상단에서 우하단까지의 경로는 n개의 a와 n개의 b를 나열하는 경우의 수와 같다.
만약 n이 2이면 경로는 a, b 문자의 조합으로 보면 각각, aabb, abab, abba, baab, baba, bbaa 로 표현할 수 있다. 
4개의 원소를 줄지우는 방법은 총 4!인데, 이 때 두 개의 a와 두 개의 b는 각각 같으므로 a끼리의 순서와 b끼리의 순서는 구분이 없다.
따라서 전체 경로의 길이는 다음 식으로 구해진다.

(w! * h!) / (w! + h!) 
"""

# from functools import reduce
#
# factorial = lambda n: reduce(lambda x, y: x*y, range(1, n+1))
# print( factorial(20+20) // factorial(20) // factorial(20))
