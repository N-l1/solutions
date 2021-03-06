"""
Warmup-1 > pos_neg
Find this problem at:
https://codingbat.com/prob/p162058
"""


def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0 and b > 0) or (a > 0 and b < 0)
