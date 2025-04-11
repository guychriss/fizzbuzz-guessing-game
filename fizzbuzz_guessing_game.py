import random
secret = random.randint(1,100)
tries = 0
max_tries = 10
score = 0
print("===Welcome to the FizzBuzz Guessing Game===")
print("Guess the secret number between 1 and 100")
print(f"You have {max_tries} tries. Good Luck ! \n ")
while tries < max_tries:
  guess = int(input(f"Try #{tries +1},Guess the secret number: "))
  tries += 1
  score= (max_tries-tries)*20
  if guess==secret :
    print("\nCorrect ! you found the secret number")
    if guess%3==0 and guess%5==0:
      score = score + 2
      print("Bonus: it's also a FizzBuzz")
    elif guess%3==0:
      score = score +1
      print("Bonus: it's also a Fizz")
    elif guess%5==0:
      score = score +1
      print("Bonus:it's also a Buzz")
    print(f"You won in {tries} tries, Your score is {score}/200 ")
    break
  else:
    score+=1
    if guess<secret :
      print("Too low,try again")
    else:
      print("Too high,try again")
    if guess%3==0 and guess%5==0:
      print("But...it's a FizzBuzz")
    elif guess%5==0:
      print("But... it's a Buzz")
    elif guess%3==0:
      print("But...it's a Fizz")
    else:
      print("Neither it's a Fizz nor it's a Buzz")
    print()
if tries==max_tries and guess!= secret:
  print(f"\nGame Over ! The secret number was {secret}.Good Luck next time")
  print(f"Your Final score: {score}/200 ") 
