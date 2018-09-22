"""
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
"""

from itertools import combinations


def is_palindrome(num_str: str) -> bool:
    # 문자열을 뒤집는 방법은 슬라이스 말고 다른 방법도 있다.
    # ''.join(list(reversed(a)))
    return num_str[::-1] == num_str


def problem_4():
    print(max(x * y for x, y in combinations(range(555, 1000), 2) if is_palindrome(str(x * y))))


problem_4()
