'''This module is meant for displaying the books along with it's details that
                    are present in the central library.'''


def books_read():
    ''' Function for reading books file and displaying them '''
    
    print('''----------------------------------------------------------------
     BOOK ID     BOOK-NAME       AUTHOR     QUANTITY   PRICE    
----------------------------------------------------------------''')
    # opening the file in reading mode
    
    books_file = open("books.txt", "r") 
    ID = 1       # giving a unique book ID for each book
    
    for line in books_file:         # for reading each line in the file
        
        # printing each line with definite tabbing
        print("\t", ID, "\t" + line.replace(",", "\t"))
        
        ID += 1      # increments the ID by 1

    # for printing the below repetative symbol
    print("----------------------------------------------------------------")
    
    books_file.close()      # closing the file


# Creating a dictionary for storing the data in books file
dist = {}

def books_dict():
    ''' Function for storing data in dictionary '''
    
    books_file = open("books.txt", "r")     # opening the file in reading mode
    ID = 1   # giving a unique ID for each book

    # reading the file line by line
    for line in books_file:
        line = line.strip("\n").split(",")      # splitting the data seperated by ','
        dist[ID] = line        # adding the list in the dictionary
        ID += 1
        
    books_file.close() # closing the file
    return dist     # returning the dictionary
