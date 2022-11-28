# EXERCISE- WATCH COCO
# ask user's name and age
# if user name start with ('a'or 'A') and age is above 10 then
# print you can watch coco movie 
# else print sorry , yuo cannot watch coco

user_name=input("enter your name please :")
user_age=int(input("enter your age please :"))
if user_age >= 10 and (user_name[0]=='a' or user_name[0]=='A'):
    print(" you can watch coco movie ")
else:
    print("you cannot watch coco")    




