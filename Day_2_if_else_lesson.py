"This Day 2 code learn python with Mahek geete"
"Lesson 1: Conditional Statements if else"
'''tokens=int(input("Enter tokens: "))

if(tokens>=1000):
    print("You can use gpt-4")
else:
    print("You can use gpt-3.5")'''

"Problem 1 Lesson conditional Statements if  else"

'''is_paid=input("Enter True if paid otherwise False: ")

if is_paid=="True":
    print("You can use gpt-4")
else:
    print("You can use gpt-3.5")'''

"Problem 2 Lesson conditional Statements if elif else"

'''model_name=input("Enter model name which you want to use:")

if model_name=="gpt-4":
    print("cost:$0.005 per 1000 tokens for gpt-4")

elif model_name=="gpt-3.5":
    print("cost:$0.002 per 1000 tokens for gpt-3.5")
else:
    print("unknown model name")'''


"Project"
'''print("Select a model do you want\n ")
print("gpt-4 tokens:1500 \n gpt-3.5 tokens:1000")
model_name=input("Enter model name which you want to use:")
tokens=int(input("Enter tokesns: "))
is_paid=input("Enter True if paid otherwise False: ")

if model_name=="gpt-4" and tokens >=1500 and is_paid=="True":
    print("You can use gpt-4")
elif model_name=="gpt-3.5" and tokens >=1000 and is_paid=="True":
    print("You can use gpt-3.5")
else:
    print("You can not use any model")'''

"Second version of project with cost calculation"
tokens=int(input("Enter tokens: "))
paid_input=input("Enter True if paid otherwise False: ")
is_paid = paid_input== "True"
model_name=input("Enter model name which you want to use gpt-4 or gpt-3.5:")

if is_paid and tokens >1000:
    print(" Access granted :You can use gpt-4")
 
else:
    print("You can use gpt-3.5")

if model_name=="gpt-4":
    cost=(tokens/1000)*0.005
elif model_name=="gpt-3.5":
    cost=(tokens/1000)*0.002
else:
    cost=0

print(f"Model : {model_name},cost:${cost}")


"Project: Number Guessing Game using if, elif, and else"
'''print("Guess the secret number from 1 to 10!")
secret_number = 7
guess = int(input("Your guess: "))

if guess == secret_number:
    print("Correct! You win!")
elif guess < secret_number:
    print("Too low! The secret number was 7.")
else:
    print("Too high! The secret number was 7.")

# Example output when the player enters 5:
# Guess the secret number from 1 to 10!
# Your guess: 5
# Too low! The secret number was 7.
#
# Explanation:
# The if branch checks whether the guess matches the secret number.
# If it does not, elif checks whether the guess is lower.
# Otherwise, else runs because the guess must be higher.'''
