"""
Warmup-1 > not_string
Find this problem at:
https://codingbat.com/prob/p1894410
"""


def not_string(str):
    if str[:3] == "not":
        return str
    return "not " + str
