# ask a user for name
# ex - harsshir 
# print count of each word
# output : 
#       h:1
#       a:2
#       r:3
#       h:4
#       i:5
#       t:6

name=input("please enter your name: ")
i=0
while i<len(name):
    print(f"{name[i]}:{name.count(name[i])}")
    i+=1