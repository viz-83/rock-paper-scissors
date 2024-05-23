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

#Write your code below this line 👇
import random
user=int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))
print("Your choice:")
if user==0:
  print(rock)
elif user==1:
  print(paper)
elif user==2:
  print(scissors)
cmp=random.randint(0,2)
print("Computer choice: ")
if cmp==0:
  print(rock)
elif cmp==1:
  print(paper)
elif cmp==2:
  print(scissors)

if user==0 and cmp==0:
  print("Its a draw")
elif user==0 and cmp==1:
  print("You lose :(")
elif user==0 and cmp==2:
  print("You win :)")
elif user==1 and cmp==0:
  print("u win")
elif user==1 and cmp==1:
  print("tie")
elif user==1 and cmp==2:
  print("u lose")
elif user==2 and cmp==0:
  print("LOSSER")
elif user==2 and cmp==1:
  print("YOU WINNN")
elif user==2 and cmp==2:
  print("TIE")
else:
  print("Learn the rules first")