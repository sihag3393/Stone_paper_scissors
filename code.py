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
rand=random.randint(0,2)
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
l=[rock,paper,scissors]
print(l[user])
print("Computer choose:")
print(l[rand])
if user==rand:
  print("Draw")
elif user==0 and rand>1:
     print("You Won")
elif user==1 and rand!=2:
    print("You Won")
elif user==2 and rand==1:
    print("You Won")
else:
   print("You Lost")
