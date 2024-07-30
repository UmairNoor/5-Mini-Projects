print("Welcome to my computer quiz! ")
playing = input("Do you want to playing the quiz game? ")

if playing.lower() !="yes":
    quit()
print("Okay! Lets play : ) ")

score = 0 

answer = input("What does CPU Stand for ? ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")

answer = input("what do you call a portable computer? ")
if answer.lower() == "laptop":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")

answer = input("What memory below is the largest? ")
if answer.lower() == "1tb":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")

answer = input("What do you do if your computer dies/malfunctions? ")
if answer.lower() == "recovery cd and recover your system":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")

answer = input("What does a Control Panel do? ")
if answer.lower() == "change settings":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")

answer = input("What is the most used search engine? ")
if answer.lower() == "google":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")

answer = input("What do you use to click stuff? ")
if answer.lower() == "mouse":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! ")

answer = input("What do you use to type? ")
if answer.lower() == "keyboard":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

print("You Got = " + str(score) + "Questions Correct! ")
print("You Got " + str(round((score/7) * 100)) + "%")