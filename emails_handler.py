
#Reads the emails from the file
def read_emails():
    list=[]
    with open("emails.txt") as f:
        list.append(f.read())    
    return list

#writes email from user to the file
def write_emails():
    while True:
        new_email = str(raw_input("Enter the email address?"))
        with open ("emails.txt", "a") as f:
            f.write('\n')
            f.write(new_email)
        to_quit = input("Do you want to enter another input? \nPress 0 to exit anyother key to continue: ")
        if(to_quit==0):
            break

        