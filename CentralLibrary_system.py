'''This is the main module of the Central Library Management System'''


# importing necessary modules for proper functioning of library system
import display
import borrowing
import returning

def library_system():
    ''' A user-defined function for user interaction. '''
    
    loop = True         # initializing loop as true

    # Printing the given statement
    print("******************************************************************")
    print("                    WELCOME TO CENTRAL LIBRARY                    ")
    print("******************************************************************")
                                                                            

    # loop that ends only on user's command
    while(loop != False):       

        # Description for using library management system
        print()     # for white space
        print("--------------------------------------------------------------")
        print("Press 'A' to see books present in the library")
        print("Press 'B' to borrow a book")
        print("Press 'C' to return a book")
        print("Press 'D' to exit the library system")
        print("--------------------------------------------------------------")
        
        # Input taken from user (A to D)
        user_input = input("Please select your task as mentioned above: ").upper()
        print()     # for empty space
        
        # Filtering the user input for A to D
        if(user_input == 'A'):
            print()
            display.books_read()       # calling the function books_read in display module   
            print()
            
        elif(user_input == 'B'):
            borrowing.books_borrow()         # calling the function books_dict in borrow module

        elif(user_input == 'C'):
            returning.books_return()     # calling the function books_return of returning module

        elif(user_input == 'D'):
            loop = False        # assigning loop as false

        else:       # error message when error found
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("     Invalid input. Please enter a letter from A to D.     ")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    # Printing statement after loop termination
    print()
    print("******************************************************************")
    print("               THANK YOU FOR VISITING THE LIBRARY                 ")
    print("******************************************************************")
    
# Calling the function library_system() created in this module  
library_system()
