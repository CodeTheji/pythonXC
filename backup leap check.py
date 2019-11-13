name = input ("Please enter your name:")
age = input ("Please enter age:")
birth_year = 2057
if(birth_year%4==0 and birth_year%100!=0 or birth_year%400==0):
    print("hello, {name}, you {age} years old, you were born in {birth_year - int(age)}, which means you are born on a leap year")
else:
    print("hello, {name}, you are {age} years old, you were born in {birth_year - int(age)}, which means you are not born on a leap year")
