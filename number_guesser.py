import random
top_of_range = input("Type a number : " )

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a larger number greater than 0 next time")
        quit()
else:
     print("Please type a larger number greater than 0 next time")
     quit()


random_number = random.randint(0,top_of_range)

while True:
    user_guess = input("Make a guess : " )
    if user_guess.isdigit():
      user_guess = int(top_of_range)

    else:
     print("Please type a larger number greater than 0 next time")
     continue
    
    if user_guess == random_number:
       print("You got it!")
       break
    else:
       print("You got it wrong!")
