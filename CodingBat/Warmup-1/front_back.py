"""
Warmup-1 > front_back
Find this problem at:
https://codingbat.com/prob/p153599
"""


def front_back(str):
    if len(str) <= 1:
        return str
    new_str = list(str)
    new_str[-1], new_str[0] = new_str[0], new_str[-1]
    return ''.join(new_str)
