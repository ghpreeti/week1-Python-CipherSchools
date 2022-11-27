# take two vomma separated inputs from user
# 1.user's name 
# 2.a string character 

# output-2 print license
# 1.user's name length
# 2.count the character that user inputed 

name,char=(input("enter name and character: ").split(','))
print(f"length of your name is {len(name)}")
print(f"character count {name.lower().count(char.lower())}")