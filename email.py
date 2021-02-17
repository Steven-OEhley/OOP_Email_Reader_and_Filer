### EMAIL APP ###

# functionality is focused on reading and filing emails

# Step 1: Import Necessary Packages

# import os
# used to check if a mail box has been set up or not
# if no mail_settings file exists then the programme will execute a mailbox set up on the first time the file is run
# if the file exists the programme will skip the set up
import os

# create lists to store emails
# created a list for inbox and spam
inbox = []
spam = []
personal_folder = []

# Step 2: Create a Class called Email

class Email():

    # Step 3: Define Attributes of the class and any methods

    # class attributes - initialsed on creation of object from the constructor
    # has_been_read and is_spam are set to default as False
    # that way they do not have to be passed in when creating an object, but can be should a user need to change the default value
    # is_spam and has_been_read default to false as later methods can be called off of an instance once the Email has been read or the Email is marked as spam by the user
    def __init__(self,from_adress,email_contents,is_spam=False,has_been_read=False):
        # the constructor can take four arguments:
        ## the adress the email was recived from  - from_adress
        ## the message or body of the email - email_contents
        ## an attribute that classifies an email as spam or not - is_spam (defaults to False on creation of instance)
        ## an attribute that classifies an email as read or not - has_been_read (defaults to False on creation of instance)
        self.from_adress = from_adress
        self.email_contents = email_contents
        self.is_spam = is_spam
        self.has_been_read = has_been_read

        # constructor also assigns an email number based on the length of the inbox + 1
        # ie len = 0 - Email assigned a number 1
        self.number = len(inbox)+1

        # on creation of instance the constructor appends the instance of the Email Class to inbox
        inbox.append(self)

    def mark_as_read(self):
        '''
        Method that can be called on an Email Instance
        Marks an email object as read
        Parameters: None
        Returns: None
        Prints: "Email has been marked as read"
        '''
        self.has_been_read = True
        print("Email has been marked as read")

    def mark_as_spam(self):
        '''
        Method that can be called on an Email Instance
        Marks an email object as Spam
        Removes instance from inbox list
        Appends instance to spam list
        Parameters: None
        Returns: None
        Prints: "Email has been marked as Spam"
        '''       
        self.is_spam = True
        inbox.remove(self)
        spam.append(self)
        print("Email marked as Spam")

    # task requires an add email method
    # email already added to inbox on creation of instance
    # add email method in my task thefore allows user to assign it to a personal folder ie work/school/finances folder
    # will ask user to create/setup mail box when the programme opens 
    # this method will allow an email to be added to that folder

    def add_email(self,target_folder):
        '''
        Method that can be called on an Email Instance
        Adds copy of Email Instance to a personal folder
        Does not remove from inbox like mark_as_spam method
        If the user would like to remove the mail from their inbox 
        after copying the email to a personal folder they can use the 
        delete email method
                
        Parameters: target folder (ie: list to append to)
        Returns: None
        Prints: "Email has been added to target_folder"
        '''  
        target_folder.append(self)
        print(f"Email has been copied to your {personal_name} folder")

    def delete_email(self):
        '''
        Method that can be called on an Email Instance
        Removes instance from inbox list
        
        Parameters: target folder (ie: list to append to)
        Returns: None
        Prints: "Email has been added to target_folder"
        '''  
        if self in inbox:
            inbox.remove(self)
            print("Email has been removed from your inbox")
        else:
            if self in spam:
                print("Mail was not in your inbox")
                print("This email is stored in your spam folder")
            else:
                print("Mail was not in your inbox")
                print("You may have already removed this item")


# Step 4: Create any Functions that would help the user navigate the interface and interact with their mail boxes

# task had asked for the following additional methods
# get email - return an email based on a given index position from the inbox
# get unread emails - return all emails that are unread
# get spam emails - return all spam emails
# get count - return the number of emails currently in the users inbox
# as these would not act on an email instance and would be used more to work with the lists
# I have created these as functions in my task
# Otherwise a user would need to call a method such as get unread off of a Email object just to return unread emails in 
# inbox list
# a task that I think would be better suited to a function as to operate it does not need to be called off of an Email class instance

def get_count(folder):
    '''
    Functions that returns the total number of Emails in the users inbox
    It also tells the user how many of these are currently unread
    Parameters: None
    Returns: None
    Prints: Total Emails and Number unread
    '''
    unread = 0
    folder_count = len(inbox)
    for email in folder:
        if email.has_been_read == False:
            unread+=1
    print(f"Your folder contains {folder_count} Emails\nOf these {unread} are currently unread")

def get_email(position,folder):
    '''
    Function displays a specific email's contents to the user
    The user can select an email based on its position in the inbox
    Parameters: position of email (ie first email = 1), expects an integer and folder name
    Returns: None
    Prints: Email Contents
    '''

    index_position = position - 1
    mail = folder[index_position]
    sender = mail.from_adress
    message = mail.email_contents


    print(
        f'''
        _________________________________
       
        Email From: {sender}
        _________________________________

        "{message}"


        ''')


def get_unread(target_folder):
    '''
    Function displays which emails in a specific folder are still unread
    Parameters: folder to find unread_emails
    Returns: list of unread emails

    '''
    unreads = []
    for mail in target_folder:
        if mail.has_been_read == False:
            unreads.append(mail)

    return unreads

# get spam function uncecessary as is_spam method 
# removes email from inbox and adds to a seperate spam list
# all spam should therefore be in this folder
# function would therefore return spam list
def get_spam_emails():
    return spam


# Step 5: Initialise Emails for User to work with

# initialised 10 Email instances 
# allow functions and methods to be tested

email_1 = Email("johnny@yahoo.com", '''
    I Thought I would send you these email tips
    Email Tips: Top 5 Strategies for Writing Effective Email
        1. Write a meaningful subject line.
        2. Keep the message focused.
        3. Avoid attachments.
        4. Identify yourself clearly.
        5.Be kind.
        ''')
email_2 = Email("data_science_daily@dsdaily.com",f'''
    Hey,

    We just thought we would mail you to let you know that you can get 25% off our DS courses.

    Hurry, these discounts wont last long!
    Secure your spot today!

    Don't waste another day struggling along, get focused and set a study goal for 2021.

    Best,
    DS Daily Team''')
email_3 = Email("buddy@gmail.com","Hey mate,\nJust checking in to see if you will be coming to my Birthday Party this Saturday?\nCheers\nBuddy")
email_4 = Email("mike@gmail.com","This is NOT SPAM!\nYou have won $200 000\nAll we require is that you pay a small fee of $15 000 to cover the tax so we can release your money\nThanks\nMike")
email_5 = Email("data_science_daily@dsdaily.com",'''
Here are some tips for choosing a great DS Role!
1. Talk to people who are already working in the industry to identify what roles are available and what each of them entails.
2. Figure out what your strengths are and what role closely aligns with your field of study and interests.
3. Find a mentor who can set aside a small amount of time to walk you through the steps you need to take.
''')
email_6 = Email("fnb_statments@fnb.co.za",f"Hi \nYour latest credit card statement is atteched\nYou owe R4200 with a payment of R800.67 due on the 01/01/2021")
email_7 = Email("jake@pc_shop.com","Hey there,\nYou asked for a sales rep to get in contact.\nHow can I help you today?")
email_8 = Email("news_breaking@bestnews.com",f"South Africa Moves Back to level 3!\nHey \nMany people have been left shattered and in tears over the fact that they cannot enjoy\na drink on New Years.\nHowever the country.....(continue reading on our website)")
email_9 = Email('jakey_boooi@jake_boi_music.com',"get my new tunes on Spotify! They are lekker!\nJakey Booooi")
email_10 = Email("lotowinuh@lotto.com","Hey you are a lotto winner - email us your id, bank card number and PIN to claim your prize")

# Step 6: Check if initial mailbox setup has been done

# check if mail_settings file exists
# if file exists - extract user info from text file (stored on initial setup)
# if no file exists take user info 
# store as mail_settings.txt file to be used when file is opened again

if os.path.isfile("mail_settings.txt"):
    # code executes if initial mail box set up has been done and reads the info from a mail_settings text file
    print("\n")
    f = open("mail_settings.txt","r")
    counter = 0
    for line in f:
        if counter == 0:
            user_name = line.strip()
            counter += 1
        elif counter == 1:
            personal_name = line.strip()
        else:
            break
else:
    # this code executes if a mail box has not been set up
    f = open("mail_settings.txt","w")
    print("\nWelcome to your new mailbox!")
    print("Lets set things up....")
    user_name = input("Please enter your first name ").strip().title()
    f.write(f"{user_name}\n")
    print(f"Thanks, {user_name}!")
    print('''
        \nNow I would like to help you set up your own folder.
        Think about folders that would help you organise your mail box.
        We will set up an inbox and spam folder automatically for you, you don't need to worry about those.
        To start off which off these folders would you like to set up:
        1. Work
        2. School
        3. Accounts
        4. Friends and Family
        ''')
    user_choice = int(input("Enter a number for a folder that you would like to create "))

    if user_choice == 1:
        personal_name = "Work"
    elif user_choice == 2:
        personal_name = "School"
    elif user_choice == 3:
        personal_name = "Acounts"
    elif user_choice == 4:
        personal_name = "Friends and Family"
    else:
        personal_name = "Personal Folder"
        print("Your choice was not valid")
        print("We have created a folder called Personal Folder for you as your input was not understood")

    f.write(f"{personal_name}")
    print(f'''
        Thanks {user_name}
        Your {personal_name} folder has been created!

        Your mail box is now all set-up.''')


# Step 7: Program Entry

# the below code simulates the users email app
# allows user to interact with Email obbjects
# Main menu - 4 options
# Each has sub menus

# Only inbox has read all unread function
# as to mark as spam or copy email email would first have to be opened before proving the user these additional choices
# ie no unread emails should exist in the Spam or persoanl folder


while True:

    # Get count of how many mails in the inbox are unread
    unread = 0
    folder_count = len(inbox)
    for email in inbox:
        if email.has_been_read == False:
            unread+=1

    # display welcome message to user
    # inform them of their unread emails

    print(
        f'''
        Welcome to your mailbox {user_name}
        You have {unread} unread emails
        ''')

    # display the main menu to the user and ask for user input

    print(
        '''
        What would you like to do?
        1. Open Inbox
        2. Open Spam
        3. Open Personal Folders
        4. Quit
        '''
        )
    
    user_choice = int(input("Enter the number the corresponds to your desired action "))

    
    # Main Menu 1 - User Inbox

    # if the user selects 1 from the main menu they will enter their inbox
    # sub menu will be dispalyed
    # user can interact with all email objects stored in the inbox list
    # all emails are added to the inbox list when they are created

    if user_choice == 1:
        
        # user provided with two options in their inbox
        # to open an indiviual mail 
        # or to read through all unread emails 1 by 1
        # looping through all unread is a quick way to get through emails
        # marks emails as read but does not allow for deleting or marking as spam
        # user needs to open an indiVidual mail for these options


        print("\nInbox Opened")
        print(
            '''
            Actions available:
            
            1. Open an Email 
            2. Display Number of Emails and Unread Emails in Inbox
            ''')
        inbox_choice = int(input("Enter that number that corresponds to your desired action "))
        # inbox choice used to know what action should be taken on the inbox

        if inbox_choice == 1:
            # if the user opens an indiviual email 
            # they can do so by passing in an index position
            # user will be presented with four further options
            # - Mark as spam, Delete, Copy to Personal folder or exit back to the main menu

            index = int(input(f"Enter the index number of the Email you would like to open from 1 to {len(inbox)} "))
            get_email(index,inbox)

            mail = inbox[index-1]
            mail.mark_as_read()

            print(
                '''
                Would you like to:
                1. Mark as Spam
                2. Delete Email
                3. Copy to your personal folder
                4. Exit to Main Menu
                ''')
            mail_action = int(input("Enter the number that corresponds to your desired action "))
            if mail_action  == 1:
                mail.mark_as_spam()
                
            elif mail_action == 2:
                mail.delete_email()
                
            elif mail_action == 3:
                mail.add_email(personal_folder)
                
            elif mail_action == 4:
                print("Returning to Main Menu")
                
            else:
                print("You did not enter a valid response")
                print("You will be returned to the main menu")
            
            continue


        elif inbox_choice == 2:
            # if the user wants to read all unread emails they can read them by opening each individually 
            # or looping through each
            # if a user opens an indivula email they can take further action
            # enetring yes will display the next unread email
            # pressing enter will return the user to the main menu
            # that way user is not forced to continue through all before being able to exit to menu

            unread_emails = get_unread(inbox)
            print(f"\nYou have {len(inbox)} and {unread} unread emails")
            print("Would you like to see an indiviual Email or open all unread? Emails")
            unread_choice = int(input(
                '''
                Enter 1 to open an indivual Email
                Enter 2 to Read All Unread Mails (Read Only - open an inidiviual mail to mark as spam or move to another folder)
                '''))
            if unread_choice == 1:
                index = int(input(f"Enter the index number of the Email you would like to open from 1 to {len(unread_emails)} "))
                get_email(index,unread_emails)

                mail = unread_emails[index-1]
                mail.mark_as_read()

                # if the user opens an indiviual email 
                # they can do so by passing in an index position
                # user will be presented with four further options
                # - Mark as spam, Delete, Copy to Personal folder or exit back to the main menu

                index = int(input(f"Enter the index number of the Email you would like to open from 1 to {len(inbox)} "))
                get_email(index,inbox)

                mail = inbox[index-1]
                mail.mark_as_read()

                print(
                    '''
                    Would you like to:
                    1. Mark as Spam
                    2. Delete Email
                    3. Copy to your personal folder
                    4. Exit to Main Menu
                    ''')
                unread_action = int(input("Enter the number that corresponds to your desired action "))
                if unread_action  == 1:
                    mail.mark_as_spam()
                    
                elif unread_action  == 2:
                    mail.delete_email()
                    
                elif unread_action  == 3:
                    mail.add_email(personal_folder)
                    
                elif unread_action  == 4:
                    print("Returning to Main Menu")
                    
                else:
                    print("You did not enter a valid response")
                    print("You will be returned to the main menu")
                    

            elif unread_choice == 2:
                print("Displaying all Unread emails\n")
                for i in range(len(unread_emails)):
                    position = i + 1
                    mail = unread_emails[i]

                    get_email(position,unread_emails)
                    mail.mark_as_read()
                    user_proceed = input("Enter 'Y' to proceed\nPress Enter to return to the Main Menu ").strip().lower()
                    if user_proceed == "y":
                        continue
                    else:
                          break
            else:
                print("You did not enter a valid response")
                print("You will be returned to the main menu")

        else:
            print("You did not enter a valid response")
            print("You will be returned to the main menu")
        
        continue







    # Main Menu - Option 2 
    # Spam Folder
    # less complex, no reason for unread options as no unread will be in this folder

    elif user_choice == 2:

        print("\nSpam Opened")
        
        # perform check incase folder is empty

        if len(spam) < 1:
            print("\nYou have no items in your Spam folder")
            print("You can mark emails in your inbox as Spam")
            print("They will be moved here when you do")
            continue

        print(
            '''
            Actions available:
            
            1. Open an Email 
            2. Display Number of Emails in Spam Folder
            ''')
        spam_choice = int(input("Enter that number that corresponds to your desired action"))
        # inbox choice used to know what action should be taken on the inbox

        if spam_choice == 1:

            # if an individual opens an email in the spam folder 
            # they can delete the email 
            # or they can move the mail to another folder
            # if they move the email is_spam attribute changes back to False

            index = int(input(f"Enter the index number of the Email you would like to open from 1 to {len(spam)} "))
            get_email(index,spam)

            mail = spam[index-1]

            # in case mail was assigned to spam with out opening
            if mail.has_been_read == False:
                mail.mark_as_read()

            print(
                '''
                Would you like to:
                1. Delete Email
                2. Move to Another Folder
                2. Exit to Main Menu
                ''')
            mail_action = int(input("Enter the number that corresponds with your desred action "))

            if mail_action == 1:
                mail.delete_email()
            elif mail_action == 2:
                target = int(input(f"Enter 1 to move to your Inbox.\nEnter 2 to move to your {personal_name} folder "))
                mail.is_spam = False
                if target == 1:
                    mail.add_email(inbox)
                    spam.remove(mail)
                elif target == 2:
                    mail.add_email(personal_folder)
                    spam.remove(mail)
                else:
                    print("You did not Enter a valid input.\nReturning to the Main Menu")

            elif mail_action == 3:
                print("Returning to Main Menu")
                
            else:
                print("You did not enter a valid response")
                print("You will be returned to the main menu")
        

        elif spam_choice == 2:
            
            print(f"\nYou have {len(spam)} spam emails")

        else:
            print("You did not enter a valid response")
            print("You will be returned to the main menu")

        continue



    # Main Menu Option 3
    # Personal Folder of User
    # Created at Email Setup - stored in mail_settings.txt
    # less complex, no need for unread email component    

    elif user_choice == 3:
        # used to get a user choice from the main menu

        print(f"\n{personal_name} Folder Opened")

        # check that folder is not empty

        if len(personal_folder) < 1:
            print(f"\nYour {personal_name} folder contains no items")
            print("You can copy an item from your inbox to your persoanl folder by opening an individual email")
            continue

        print(
            f'''
            Actions available:
            
            1. Open an Email
            2. Display the number of emails in your {personal_name} folder
            
            ''')
        personal_choice = int(input("Enter that number that corresponds to your desired action "))
        # personal_choice used to know what action should be taken on the inbox

        if personal_choice == 1:
            index = int(input(f"Enter the index number of the Email you would like to open from 1 to {len(personal_folder)} "))
            get_email(index,personal_folder)

            mail = personal_folder[index-1]
            mail.mark_as_read()

            print(
                '''
                Would you like to:
                1. Delete Email
                2. Send to Spam
                3. Exit to Main Menu
                ''')
            mail_action = int(input("Enter the number that corresponds to your desired action "))
            if mail_action  == 1:
                mail.delete_email()
                
            elif mail_action == 2:
                mail.mark_as_spam()
                personal_folder.remove(self)
                          
            elif mail_action == 3:
                print("Returning to Main Menu")
                
            else:
                print("You did not enter a valid response")
                print("You will be returned to the main menu")
            
        

        elif personal_choice == 2:
            print(f"Your {personal_name} folder contains {len(personal_folder)} emails") 


        else:
            print("You did not enter a valid response")
            print("You will be returned to the main menu")
        
        continue



    # Main Menu Choic 4

    # allows user the option to quit the programme

    elif user_choice == 4:
        print("\nShutting Down Mail Box - Goodbye!")
        break


    # allows user another attempt in the event that they did not enter valid input.
    
    else:
        print("\nNo valied response received")
        print("Try again")
        continue


# close file that checks if mailbox has already been set up
f.close()
