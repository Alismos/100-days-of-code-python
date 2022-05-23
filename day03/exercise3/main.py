# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

rule1 = year % 4
rule2 = year % 100
rule3 = year % 400
if(rule1 == 0):
    if(rule2 == 0):
        if(rule3 == 0):
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
