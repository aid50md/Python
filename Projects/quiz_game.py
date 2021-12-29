print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play:) ")
# create a score variable and inititialize
score = 0

answer = input("What does CPU stand for? ") # alternately .lower()
if answer.lower() == "central processing unit":
    print('Correct!') 
    score += 1
else:
    print('Incorrect')

# 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!') 
    score += 1
else:
    print('Incorrect')

# 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!') 
    score += 1
else:
    print('Incorrect')

# 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!') 
    score += 1
else:
    print('Incorrect')

# tally the user score
print('You got ' + str(score) + ' questions correct!')
# print('You got ' + str((score / 4) * 100)  + ' percent correct!')
print('You got ' + str((score / 4) * 100)  + '%.')
