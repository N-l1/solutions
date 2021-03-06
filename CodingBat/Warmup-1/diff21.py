"""
Warmup-1 > diff21
Find this problem at:
https://codingbat.com/prob/p197466
"""


def diff21(n):
    if n > 21:
        return abs(2*(n-21))
    return abs(n - 21)
