'''This is the module for getting the date and time from the system of the user
      for recording books transact with exact date and time in library.'''


# import the in-built python library datetime 
import datetime 

# calling the now() function in datetime 
clock = datetime.datetime.now()

def pc_date():
    ''' function for fetching the date '''
    
    # calls the date() function in the datetime library
    d = clock.date()
    return ("Date: " + str(d))          # returns the date of the transact day

def pc_time():
    ''' function for fetching the time '''
    
    # calls the time() function in the datetime library for time in hours, minutes and seconds
    t = clock.strftime("%H:%M:%S")
    return ("Time: " + str(t))          # returns the time during the transact

def borrow_date(file_lines):
    ''' parameterized function for fetching date from borrowed bills '''
    
    for line in file_lines:         # reading each lines in a file
        if "Date: " in line:    # filtering the line containing date
            row = line.split()          # splitting every contains in the specified line
            each = row[-1].split("-")       # splitting the element through '-'
            
            # finding the difference between year, month and second
            year = datetime.datetime.now().year - int(each[0])  # for year
            month = datetime.datetime.now().month - int(each[1])    # for month
            day = datetime.datetime.now().day - int(each[2])      # for day
            total_days = year*365 + month*30 + day      # total days count

    return total_days               # returning the days counted
