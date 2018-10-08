"""
n의 약수들 중에서 자신을 제외한 것의 합을 d(n)으로 정의했을 때,
서로 다른 두 정수 a, b에 대하여 d(a) = b 이고 d(b) = a 이면
a, b는 친화쌍이라 하고 a와 b를 각각 친화수(우애수)라고 합니다.

예를 들어 220의 약수는 자신을 제외하면 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 이므로 그 합은 d(220) = 284 입니다.
또 284의 약수는 자신을 제외하면 1, 2, 4, 71, 142 이므로 d(284) = 220 입니다.
따라서 220과 284는 친화쌍이 됩니다.

10000 이하의 친화수들을 모두 찾아서 그 합을 구하세요.
"""

"""
약수의 합을 구하는 부분에서 시간을 단축할 수 있다.
https://soooprmx.com/archives/6336
"""


def sum_divisor(n):
    res = 0
    for i in range(1, n // 2 + 1):
        if n % i is 0:
            res += i
    return res


def get_affinity(a):
    b = sum_divisor(a)
    if b != a and sum_divisor(b) == a:
        return b
    return None


affinity_set = set()


def problem21():
    for a in range(2, 10001):
        b = get_affinity(a)
        if b is not None:
            affinity_set.add(a)
            affinity_set.add(b)

    print(sum(affinity_set))


problem21()

# {1184, 6368, 5564, 5020, 2924, 284, 6232, 1210, 220, 2620}
