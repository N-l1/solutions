"""
Warmup-1 > front3
Find this problem at:
https://codingbat.com/prob/p147920
"""


def front3(str):
    if len(str) < 3:
        return 3 * str[:len(str)]
    return 3 * str[:3]
