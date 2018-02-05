import random                                                                   # importing random module for random number of Dice                                                               # Setting a condition for continuous looping
def rolling():                                                                  # Function Definition
    ans = str(input('Do you want to roll the Dice\n'))                          # Getting user input
    while True:                                                    # Setting while statement to make sure the function loops until the Pre_req condition is false
        Pre_req = 'True'
        if ans.lower() == 'yes':                                                # checking whether user input is yes
            x = random.randrange(1, 7)                                          # assigning random number to variable
            print('\nThe number on the Dice is: ', str(x))                      # print statement
            Pre_req = 'True'
            rolling()
            break                                                           # function call for repetition
        else:
            Pre_req = 'False'                                                   # Setting value to loop out of the function
            print('Thanks for playing')
            break

rolling()
