"""
피보나치 수열은 아래와 같은 점화식으로 정의됩니다.

Fn = Fn-1 + Fn-2  (단, F1 = 1, F2 = 1).
이에 따라 수열을 12번째 항까지 차례대로 계산하면 다음과 같습니다.

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
수열의 값은 F12에서 처음으로 3자리가 됩니다.

피보나치 수열에서 값이 처음으로 1000자리가 되는 것은 몇번째 항입니까?
"""

"""
어떤 수 x에 대해서 10을 밑으로 하는 로그를 취하면 그 정수값 + 1을 하게 되면 자리수가 된다.
이를 이용하여 math 모듈의 log10 을 이용해도 된다.
if log10(n) >= 999
ref) https://soooprmx.com/archives/6388
"""


def gen_fib():
    a, b = 0, 1
    yield b
    while True:
        yield a + b
        a, b = b, a + b


ten_power_ten = pow(10, 999)
count = 1
for n in gen_fib():
    if n // ten_power_ten >= 1:
        break
    count += 1

print(count)
