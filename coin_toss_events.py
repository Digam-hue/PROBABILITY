"""
How can we generate all possible outcomes for tossing a set of coins
and then find the number of outcomes that match a specific condition,
like getting exactly 2 Heads?
"""

import random

coin_faces = ['H', 'T']
sample_space = []
unique_outcomes_found = 0

num_coins = int(input('Enter how many coins you want to toss at a time: '))

print("\n the sample space")

while unique_outcomes_found < (2 ** num_coins):
    current_toss = []
    for _ in range(num_coins):
        current_toss.append(random.choice(coin_faces))
    
    if current_toss not in sample_space:
        sample_space.append(current_toss)
        unique_outcomes_found += 1

print("\n--- Complete Sample Space ---")
for outcome in sample_space:
    print(outcome)
print(f"Total possible outcomes: {len(sample_space)}")
print("-" * 40)

user_input = input("Enter the event to find (e.g., '2 H' for exactly 2 Heads): ")
count_str, face_to_find = user_input.split()
required_count = int(count_str)
face_to_find = face_to_find.upper()

event_matches = 0
print(f"\nOutcomes with exactly {required_count} '{face_to_find}':")

for outcome in sample_space:
    if outcome.count(face_to_find) == required_count:
        print(outcome)
        event_matches += 1

print(f"\nFound {event_matches} matching outcomes.")
