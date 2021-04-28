import random
number = random.radiant(1,9)
chance=0
print("guess a number from 1 to 9")
while chance < 5:
      guess = int(input("enter the number you thought of "))
if guess == number:
    print("Conratulations, you won.")
    break

elif guess<number:
     print("Failed , You should guess a higher number")
else:
     print("Failed , You should guess a lower number")

     chance+=1

     if not chance < 5 :
          print("You loose, the number was" , number)