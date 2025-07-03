guess_num=5
guess_count=0
while True:
    guess_user=int(input("Guess the number:"))
    if guess_user==guess_num:
        print("You Won")
        break
    else:
        guess_count+=1
        if guess_count==3:
            print(f"You lost..{guess_num} is the number")
            break
        else:
            print("Try again")