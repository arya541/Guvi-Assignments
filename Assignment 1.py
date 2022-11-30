import re
import csv

mailId_char = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
pass_char = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*#?&])[A-Za-z0-9@$!#%*?&]{5,17}$")


def validEmailId(email_Id):
    if re.fullmatch(mailId_char, email_Id):
      return True
    else:
      return False

def validPwd(password):
    if len(password) > 5 and len(password) < 16 and re.fullmatch(pass_char, password):
      return True
    else:
      return False

def write_into_file(email_Id, password , mode = 'a', newline = ''):
    with open('userList.csv', mode, newline = newline) as op:
        writer = csv.writer(op)
        writer.writerow([email_Id, password])
        

def fileSearch(email_Id, password , mode = 'r', newline = ''):
    with open('users.csv', mode,  newline = newline) as opf:
        reader = csv.reader(opf)
        for row in reader:
            if email_Id == row[0] and password == row[1]:
                return True
        return False

def passwordSearch(email_Id, mode = 'r', newline = ''):
    with open('users.csv', mode,  newline = newline) as opp:
        reader = csv.reader(opp)
        for row in reader:
            if email_Id == row[0]:
                print('\nPassword for '+ email_Id + ' is '+ row[1])
                return True
        return False

def register():
    print('\nNew User Registration\n')
    email_Id = input('email id: ')
    if validEmailId(email_Id):
        password = input('password: ')
        if validPwd(password):
            write_into_file(email_Id, password)
            print('\nUser Registered Successfully')
        else:
            print('\nInvalid Password.')
    else:
        print('\nInvalid Username.')


def login():
    email_Id = input('email id: ')
    if validEmailId(email_Id):
        password = input('password: ')
        if validPwd(password):
            if fileSearch(email_Id, password):
                print ('\nUser Logged In Successfully')
            else:
                print('\nUser Not Found')
                register()
        else:
            print('\nInvalid Password.')
    else:
        print('\nInvalid Username.')

def forgot_pwd():
    email_Id = input('email id: ')
    if validEmailId(email_Id):
        if passwordSearch(email_Id):
            print ('\nUser Logged In Successfully.')
        else:
            print('\nUser Not Found')
            register()
    else:
        print('\nInvalid Username.')

        


if __name__ == "__main__":
    while True:
        print('''a) New User Registration
                b) Existing User Login
                c) Forgot Password
                ''')
        value = input()
        if value == 'a':
            register()
        elif value == 'b':
            login()
        elif value == 'c':
            forgot_pwd()
        else:
            print("Invalid Option")