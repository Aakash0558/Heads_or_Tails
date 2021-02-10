import random

user_input = input("This is random coin toss generator. Please select one of Heads or Tails: ").lower()
toss = random.randint(0,1)
toss_input = 0

if toss == 1:
  toss_input = "Heads"
elif toss == 0:
  toss_input = "Tails"

if user_input == toss_input.lower():
  toss_input.capitalize()
  print(f"It is {toss_input}. You have won the toss!")
else:
  toss_input.capitalize()
  print(f"It is {toss_input}. You have lost the toss")
