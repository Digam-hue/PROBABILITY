"""
Estimate the probability of getting 'head' using large-scale simulation.
This runs n random coin tosses and calculates the experimental probability.
"""

import random

coins = ['head', 'tail']
n = 1000000
head_count = 0

for _ in range(n):
    if random.choice(coins) == 'head':
        head_count += 1

print('Total tosses:', n)
print('Count of heads:', head_count)
print('P(head) :', (head_count / n) * 100, '%')
