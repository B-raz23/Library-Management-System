'''This module is meant for handling the several tasks for borrowing a book
                           from the central library.'''


# importing the necessary modules for proper function
import date_time
import display

def books_borrow():
    ''' Function for borrowing books '''
    
    books = display.books_dict()    # assigning books the value returned by books_dict function

    print()
    # taking the name and library ID of the borrower
    name = input("Full Name of the borrower: ").upper()
    while(True):    # infinite loop
        try:
            lib_ID = int(input("\nEnter your library ID: "))
            break
        except:
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("           Library ID's are integer values !!          ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
    param_name = "Borrower- " + name  # concatinating strings
    bill(name, param_name, lib_ID)          # calling the function bill() of same module with a parameter
    
    total_cost = 0      # initializing total cost as 0
    note = []         # creating a list for generating note
    
    # infinite loop
    while(True):
        print()     # empty line
        display.books_read()        # calling the function in display module

        # using concept of exception handling for exceptions elimination
        try:
            # User-input for book id
            print()     
            given_ID = int(input("Enter the Book ID of the book to borrow as shown: "))
            print()

            # verifying the entered book ID
            if(given_ID > 0 and given_ID < 8):
                book = books[given_ID]      # fetching value of a desirable key 
                qnt = int(book[2])      # storing the quantity of a given book

                if(book[0] not in note):
                    # if the required book is present
                    if(qnt > 0):
                        # gives availability message
                        print()
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("                 Book is available !!                  ")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print()

                        note.append(book[0])  # appends the borrowed books name in the list
                        qnt -= 1     # reduces the quantity of the book borrowed

                        # saves the reduced quantity in the dictionary
                        books[given_ID] = [book[0], book[1], str(qnt), book[3]]
                        
                        file = open("books.txt", "w")   # opens file in writing mode

                        # writing all the data in the file from the updated dictionary
                        for value in books.values():
                            file.write(str(value[0])+","+str(value[1])+","+str(value[2])+","+str(value[3]))        
                            file.write("\n")
                        file.close()        # closing the opened file

                        # opening another created file in append mode for generating a bill
                        f = open(record, "a")
                        f.write("   "+str(given_ID)+"\t\t"+str(book[0])+"\t\t"+str(book[1])+"\t\t"+str(book[3])+"\n")
                        f.close()

                        # adding cost of each borrowed book for the total cost 
                        total_cost = total_cost + float(book[3].strip('$'))
                        
                        # asks whether the borrower needs another book or not
                        print("Do you want to borrow more books?")
                        loop = input("If yes enter 'Y' or else give any other input: ").upper()
                        print()
                        if(loop != "Y"):    # if not needed another book
                            # again opening the file in append mode for finalizing of the bill
                            f = open(record, "a")   
                            f.write("\n---------------------------------------------------------------------\n")
                            # writing the added cost of total borrowed books to the file
                            f.write("\n\t\t\t\t\t\t  "+"Grand Total: "+"$"+str(total_cost))
                            f.close()
                            break       # terminates the loop

                    else:       # when required book is not in library
                        # display a suitable message
                        print()
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("               Book is not available !!                ")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print()

                else:
                    print()
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("            Can't borrow same book twice !             ")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print() 
                            
            else:   # if the ID given is incorrect
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("            Please enter a valid Book ID !!            ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                   
        except:     # if user enters any other characters except the numeric
            print()
            print()
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("       Invalid input. Please enter a numeric value.        ")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print()
            print()

    # Printing the details for a success borrow       
    print()
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("                     Customer Borrow Details                       ")
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("\nName of Customer: ", name)
    print(date_time.pc_date())
    print(date_time.pc_time())
    print("\nBooks borrowed are: ")
    for each in note:        # iterating through the list li and priting it's elements
        print(each)    # printing the list elements one by one
    print()
    print("Total price for borrow: " + "$" + str(total_cost))      # prints the total cost
    print("\n'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")


def bill(name, file_name, lib_ID):
    ''' Function for generating the bill '''
    
    global record   # declaring record as global for easy access
    
    # creating a new file based on name and ID of borrower
    record = "transaction bills/" + file_name + "[" + str(lib_ID) + "]" + ".txt"
    f = open(record, "w+")  # opening the created file in "w+" mode

    # Several things are written to the file with proper spacing
    f.write("\t\t\t CENTRAL LIBRARY INVOICE \n")
    f.write("\t\t\t   ( Rayale-09, Kavre ) \n\n\n")
    f.write(date_time.pc_time())        # calling the date function in datetime module
    f.write("\t\t\t\t\t    " + date_time.pc_date() + "\n\n")      # calling time function for the time
    f.write("\t\t        Name: " + name + "\n\n\n")
    f.write("---------------------------------------------------------------------\n")
    f.write("Book ID" + "\t        Book Name" + "\t\t Author" + "\t\t       Price \n")
    f.write("---------------------------------------------------------------------\n")
    f.close()   # closing the file

    return record
