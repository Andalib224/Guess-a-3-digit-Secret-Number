import random, os

os.system('cls')

List_of_number=[0,1,2,3,4,5,6,7,8,9]

secret_number=""
for _ in range(0,3):
    list_value=random.choice(List_of_number)
    secret_number +=str(list_value)

guess_attempt=False
attempt=1

def number_checking(secret_number, entered_number):
    
    not_found_digit_count=0
    digit_match=""

    if (secret_number == entered_number):
        print(f"You got it and Secret number is {secret_number}",end=" ")
        digit_match=secret_number
    elif secret_number != entered_number:

        for num2 in entered_number:
            
            if num2 in secret_number:
                idx_secrect_number=secret_number.index(num2)
                idx_entered_number=entered_number.index(num2)

                if (idx_secrect_number == idx_entered_number ):
                    print("Fermi",end=" ")
                    
                elif (idx_entered_number != idx_secrect_number ):
                    print("Pico",end=" ")
                    

            elif num2 not in secret_number:
                not_found_digit_count +=1

                if not_found_digit_count == 3 :
                    print("No digit is correct",end=" ")
            
        
    print(end='\n')  

    return digit_match    

def play_again():
    should_continue=input("Do you wish to play again? (yes or no): ")  
    return should_continue   

def game_info():
    print(f"Bagels, a deductive logic game")
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print('''
    When I say: That means:
    Pico One digit is correct but in the wrong position.
    Fermi One digit is correct and in the right position.
    Bagels No digit is correct.
    ''')   

game_info()      

while not guess_attempt:
    print(f"guess #{attempt}")
   
    try:
        entered_number=int(input("Please entered a 3-digit number: "))
    except ValueError:
        print("Input Number is not Integer type")
    else:
        
        entered_number_as_str=str(entered_number)
        if (len(entered_number_as_str) == 3):
            all_digit_match=number_checking(secret_number, entered_number_as_str)

            if all_digit_match == entered_number_as_str and attempt <10:
                is_play_again=play_again()
                

                if is_play_again == 'yes':
                    game_info()
                    attempt = 0

                elif is_play_again == 'no':
                    print("Thank you for playing it. ")
                    guess_attempt = True
            

            attempt +=1
            if (attempt == 10):
                is_play_again=play_again()
                if is_play_again == 'yes':
                    game_info()
                    attempt = 0
                else:
                    print("Thank you for playing it. ")
                    guess_attempt = True
        
        elif (len(entered_number_as_str)!=3):
            print("Please enter a 3-digit number")
            attempt +=1

    
        
        


