# 10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.
# 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

# 1
def multiples_of_3_and_5_1(n):
    res = 0
    for i in range(n):
        if i % 3 is 0:
            res += i
        elif i % 5 is 0:
            res += i

    return res


# 2
def multiples_of_3_and_5_2(n):
    return sum((x for x in range(1, n) if x % 3 is 0 or x % 5 is 0))


# 3
def multiples_of_3_and_5_3(n):
    t = (n - 1) // 3
    f = (n - 1) // 5
    x = (n - 1) // 15
    return 3 * t * (t + 1) / 2 + 5 * f * (f + 1) / 2 - 15 * x * (x + 1) / 2


print(multiples_of_3_and_5_1(1000))  # 233168
print(multiples_of_3_and_5_2(1000))  # 233168
print(multiples_of_3_and_5_3(1000))  # 233168
