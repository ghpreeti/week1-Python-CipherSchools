# problem
# ask user input more than one digit
# ex=1234
# calculate 1+2+3+4
   


#    algorithm metod to solve problem in human language
#    dont change to int 
#    ex-"1256"
#    pick caracter one by one and change to int
#    int(ex[0]+int(ex[1])......go upto len(ex))
  
num=input("enter a number : ")  

total=0
i=0
while  i<len(num):
    total += int(num[i])
    i+=1
print(total)    
