# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name_together = name1.lower() + name2.lower()

num1 = name_together.count("t") + name_together.count("r") + \
    name_together.count("u") + name_together.count("e")

num2 = name_together.count("l") + name_together.count("o") + \
    name_together.count("v") + name_together.count("e")

score = int(str(num1) + str(num2))

if(score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
