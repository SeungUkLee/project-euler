"""
문제
1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
"""

"""
접근
최소 공배수 문제이다.
일단 세 수 a, b, c 의 최소 공배수를 어떻게 구하는지 알아야한다. 
우선 a, b 의 최소 공배수를 구한다. 이를 lcm_1 이라고 하자. 
그다음 lcm_l 과 c 의 최소 공배수를 구하면 세 수의 최소 공배수가 구해진다. -> reduce() 
최소 공배수는 다음과 같이 구할 수 있다.
a = Gx, b = Gy (G는 a,b 의 최대 공약수) 이라고 하면
a * b = G * G * x * y
최소 공배수는 G * x * y 
따라서 lcm(a,b) = (G * x) * (y) = (a) * (b/gcd(a,b))

최대 공약수는 유클리드 호제법을 이용하는 것이 빠르다. -> https://opentutorials.org/course/1685/9533
f(a, b) = gcd(a, b)라 합시다. 
이 때 a mod b = 0 이라면, f(a, b) = b임이 자명함을 알 수 있습니다. 
이 때 a mod b이 0이 아닌 경우, f(a, b) = f(b, a mod b)가 성립하고, 이를 유클리드 호제법이라고 합니다.
"""

from functools import reduce


def gcd(a: int, b: int) -> int:
    mod = a % b
    while mod > 0:
        a, b = b, mod
        mod = a % b
    return b


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


print(reduce(lcm, range(1, 21)))
