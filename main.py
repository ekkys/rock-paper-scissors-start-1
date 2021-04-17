rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

my_choice = input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n")
# Masukkan variable kedalam list
choice = [rock, paper, scissors]
mera_choice= int(my_choice)
#print my choice
print(choice[mera_choice])

#bot vhoice
bot_choice = random.randint(0, 2)

#print bot choice
print(choice[bot_choice])

if mera_choice == bot_choice:
  print("Draw")
elif mera_choice < bot_choice:
  print("You Win!")
else:
  print("You Loose!")