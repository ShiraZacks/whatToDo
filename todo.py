# question!!

print("Do you want to go out this weekend? (Y/N)")
answer = input()

#if wants to go out or not...

if(answer == "Y"):
    print("Is the weather going to be sunny? (Y/N)")
    answer = input()

# if nice outside or not...

    if(answer == "Y"):
        print("Do you like group sports? (Y/N)")
        answer = input()

    # if wants sports or not...

        if(answer == "Y"):
            print("Go play Football!")
        else:
            print("Go play Tennis!!")

    #if wants to move or not...

    else:
        print("Would you like to move? (Y/N")
        answer = input()
        if(answer == "Y"):
            print("Go dancing!")
        else:
            print("Go to the movies!!")

# if wants to stay in...

else:
    print("Do you want to be alone? (Y/N)")
    answer = input()

# if wants company or not...
    
    if(answer == "Y"):
        print("Do you want to move? (Y/N)")
        answer = input()

    # if wants to move or not

        if(answer == "Y"):
            print("Do some excercise!!")
        else:
            print("Watch some Netflix!")

# if wants to hang out with people or not....   

    else:
        print("Do you have a place to host? (Y/N")
        answer = input()
        if(answer == "Y"):
            print("Plan a party!")
        else:
            print("Visit a friend!")
