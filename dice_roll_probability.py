"""
How can we simulate rolling multiple dice and calculate the probability
of getting a specific outcome — for example, the number of times we roll a 6?
"""

import random

dice_faces = [1, 2, 3, 4, 5, 6]
count = 0

num_dice = int(input('Enter how many dice you want to toss at a time: '))

for _ in range(num_dice):
    roll = random.choice(dice_faces)
    if roll == 6:
        count += 1

print('Number of sixes rolled:', count)
print('P(6) :', count / num_dice)
