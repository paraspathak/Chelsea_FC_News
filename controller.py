# coding: utf-8
import logging
while True:
    try:
        #First we run the spider to get the info from the website
        from subprocess import call
        call(["scrapy","crawl", "wagnh", "-o", "data.csv"])     #store in the form of data.csv

        #------------------------
        #secondly we read the file
        import os
        import fileinput
        total_website_data ='Chelsea News from Weaintgotnohistory.sbnation.com\n'
        last_title_emailed = ''     #to store the last title if you want to minimze emails
        counter = 1
        with open("data.csv","r") as f:
            for line in f:
                if(counter!=1):
                    if counter == 2:
                        last_title_emailed = line
                    total_website_data+=line
                    counter+=1
                else:
                    counter+=1
        #print(total_website_data)
        print("Last statement emailed is", last_title_emailed)

        #------------------------
        #third load all the emails from the file
        import emails_handler
        print("Current Users in databse are:\n")
        users = emails_handler.read_emails()
        for user in users:
            print(user)
        """
        to_add = input("Do you want to add more users?\nPress 1 to ADD: ")
        if(to_add==1):
            emails_handler.write_emails()
        """
        #------------------------
        #fourth we email the file
        import send_email

        email = send_email.Email_Sender()
        email.user_to_send_to = users
        email.send_email(total_website_data, "Chelsea Headlines")

        #delete the file so as to prevent further addition
        import os
        os.remove("./data.csv")

        #make the program sleep for 1 day

        import time
        time.sleep(86400)  #make it sleep for 1 day (24 hours)
    except Exception as e:
        logging.error(e)
