#TAKING BIO DATA THAT WOULD INDICATE IF YOU WERE BORN ON A LEAP YEAR
name = input ("Please enter your name:")
age = input ("Please enter age:")
current_year = 2019
if(current_year%4==0 and current_year%100!=0 or current_year%400==0):
    comment =f"Hello {name}, you are {age} years old, born on {current_year - int(age)}, which means you were born on a leap year"
else:
    comment =f"Hello {name}, you are {age} years old, born on {current_year - int(age)}, which means you were not born on a leap year"
print(comment)