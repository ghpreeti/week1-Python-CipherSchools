# EXERCISE,NUMBER GUESSING GAME
# Make a variable , likenwinning number and assing any number
# ask user to guess a number
# if user guessed correctly then print "you win !!"
# if lower print "too low"
# if higher than print "too high"
winning_number=27
user_input= int(input("guess a number btw 1 to 100"))
if user_input==winning_number:
    print("YOU WIN!!")
else:
    if user_input<winning_number:
        print("too low")
    else:
        print("too high")    
