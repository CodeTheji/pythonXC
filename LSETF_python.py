# # 1*1
# # print(1*1)
# # mynumber = 20.234
# # rounded_num = round(mynumber, 2)
# # print (rounded_num)
# # num = 22
# # dem = 7
# # pi = num / dem
# # print(pi)
# # rounded_num = round(pi, 3)
# # print(rounded_num)
# # name = "Elson John"
# # phone = 8023245312 * 6
# # print(phone)
# # name = "Elson"
# # surname = "John"
# # fullname = name +" " + surname
# # print(fullname)
# # day = "20"
# # month ="May"
# # year = "2019"
# # print(day +" " + month+", " + year)
# # pi = 22/7
# # statement = "pi is" + str(pi)
# # print(statement)
# # statement = "pi is " + str(round(pi, 2))
# # print(statement)
# # print(round(pi, 2))
# akara = input ("Please how many akara do you want?")
# akamu = input ("Please how many akamu do you want?")
# print(akara, akamu)
# akara_statement = "You bought" + akara + "akamu"
# akamu_statement = "You bought" + akamu + "akara"
# print(akara_statement)
# print(akamu_statement)
# akara_price = 20
# akamu_price = 50
# bill = "Your bill is : " + str(int(akara) * akara_price + int(akamu) * akamu_price) # note, str was added and all placed within a bracket, so it could all be in string
# print(bill)

#TAKING IN BOI DATA

name = input ("Please enter your name:")
age = input ("Please enter age:")
birth_year = 2019
if(birth_year%4==0 and birth_year%100!=0 or birth_year%400==0):
    comment =f"Hello {name}, you are {age} years old, you were born in {birth_year - int(age)}, which means you were born on a leap year"
else:
    comment =f"hello {name}, you are {age}, you were born in {birth_year - int(age)}, which means you were not born on a leap year"
print(comment)
