'''This module is meant for handling the several tasks for returning a book
                           from the central library.'''


# importing the necessary modules for proper function
import date_time
import display
import borrowing

def books_return():
    ''' User-defined function for returning books '''
    
    books = display.books_dict()        # assigning books the value returned by books_dict function
    borrowed_list = []      # list for book ID in the file
    
    # taking the name of the borrower as input
    while(True):        # infinite loop
        # exception handling for any occured exceptions
        try:    
            print() # taking name as input
            name = input("Full Name of the borrower: ").upper()
            while(True):  # loop until correct
                # exception handling for number format exception
                try:
                    # input for library ID 
                    lib_ID = int(input("\nEnter your library ID: "))
                    break
                except:
                    # if exception found
                    print()
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("           Library ID's are integer values !!          ")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                
            # reading the borrowed file based on name of borrower
            borrow_file = "transaction bills/Borrower- " + name + "[" + str(lib_ID) + "]" + ".txt"
            read_file = open(borrow_file, "r")  # opening the created file in reading mode    
            print("\n\n\n\n" + read_file.read() + "\n\n\n\n")
            read_file.close()

            # again opening the borrowed file for books ID
            read_again = open(borrow_file, "r")
            line = read_again.readlines()   # read the file line by line
            # loop for the books content
            for line_num in range(12, len(line)-4):
                for iD in line[line_num].split():       # fetches each element of a specified index
                    borrowed_list.append(int(iD))   # appending eah book id in the borrowed file
                    break   # terminates the loop
            read_again.close()
            # calling the function in date_time module
            duration = date_time.borrow_date(line)
            
            break
            
        except:     # for invalid name or id given
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("         Invalid Name or Library ID provided !!        ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()

    param_name = "Returner- " + name    # concatinating strings
    record = borrowing.bill(name, param_name, lib_ID)    # calling the function bill() of borrowing module with a parameter
    
    # initializing borrow cost total cost and fine as 0
    borrow_cost = 0
    fine = 0
    total_cost = 0
    note = []         # creating a list used in generating note

    # infinite loop
    while(True):
        # using concept of exception handling for exceptions elimination
        try:
            # User-input for book id
            print()     
            given_ID = int(input("From the bill shown, enter the book ID for returning: "))
            print()

            # verifying the entered book ID
            if(given_ID not in borrowed_list):
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("    Please enter a valid Book ID as shown in bill !!   ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()

            else:   # if the ID given is correct
                book = books[given_ID]      # fetching value of a desirable key 
                qnt = int(book[2])      # storing the quantity of a given book
                
                if(book[0] not in note):
                    note.append(book[0])  # appends the returned books name in the list
                    qnt += 1     # increases the quantity of the book returned

                    # saves the increased quantity in the dictionary
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

                    # updating cost and fine of the books for payment 
                    borrow_cost = borrow_cost + float(book[3].strip('$'))
                    
                    # asks whether the returner wants to return another book or not
                    print("\nDo you want to return other books that you borrowed?")
                    loop = input("If yes enter 'Y' or else give any other input: ").upper()
                    print()
                    
                    if(loop != "Y"):    # if not returned another book
                        if(duration > 10):
                            fine = (5/100)* borrow_cost * duration # fine calculation on basis of late return
                            
                        total_cost = borrow_cost + fine
    
                        # again opening the file in append mode for finalizing of the bill
                        f = open(record, "a")   
                        f.write("\n---------------------------------------------------------------------\n")
                        # writing the costs to the file
                        f.write("\n\t\t\t\t\t    "+"Price for borrow: "+"$"+str(borrow_cost))
                        f.write("\n\t\t\t\t\t        "+"Fine charged: "+"$"+str('%.2f' % fine))
                        f.write("\n\t\t\t\t\t         "+"Grand Total: "+"$"+str('%.2f' % total_cost))
                        f.close()
                        break       # terminates the loop
                else:
                    print()
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("            This book is already returned !            ")
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

    # Printing the details for a success return      
    print()
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("                     Customer Return Details                       ")
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("\nName of Customer: ", name)
    print(date_time.pc_date())
    print(date_time.pc_time())
    print("\nBooks returned are: ")
    for each in note:        # iterating through the list note and priting it's elements
        print(each)    # printing the list elements one by one
    print()
    print("Price for borrow: " + "$" + str(borrow_cost))   # prints the cost for borrow   
    print("Fine for delayed return: " + "$" + str('%.2f' % fine))  # prints the fine charged
    print("Grand Total: " + "$" + str('%.2f' % total_cost))   # prints the total cost
    print("\n'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
