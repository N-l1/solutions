"""
Warmup-1 > parrot_trouble
Find this problem at:
https://codingbat.com/prob/p166884
"""


def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)
