"""
Generate and display sample spaces for:
1. Two coin tosses
2. Two dice rolls
3. One coin toss and one dice roll together
4. Random outcomes using random module
"""

import random

coins = ['H', 'T']

print("\nTotal sample space from 2 coin tosses:")
for i in coins:
    for j in coins:
        print(i + j, end=" ")

print("\n\nTotal sample space from 2 dice rolls:")
for i in range(1, 7):
    for j in range(1, 7):
        print(f"({i},{j})", end=" ")

print("\n\nSample space from tossing a coin with rolling a dice:")
for i in range(1, 7):
    for j in coins:
        print(f"({i},{j})", end=" ")

print("\n\nRandom outcome from 2 coin flips:")
print(random.choice(coins), random.choice(coins))

print("\nRandom outcome from 2 dice rolls:")
print(f"({random.randint(1,6)}, {random.randint(1,6)})")
