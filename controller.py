# coding: utf-8
import logging
while True:
    try:
        #First we run the spiders to get the info from the website
        from subprocess import call
        call(["scrapy","crawl", "wagnh", "-o", "data.csv"])     #store in the form of data.csv
        call(["scrapy","crawl", "links", "-o", "link.csv"])     #store the links in the form of link.csv

        #------------------------
        #secondly we read the file
        import parse_csv
        #get the formatted html texts combining links and headline to email
        total_website_data = parse_csv.parsed_html('link.csv','data.csv',10)

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
    except Exception as e:
        logging.error(e)
    finally:
        #delete the file so as to prevent further addition
        import os
        os.remove("./data.csv")
        os.remove("./link.csv")

        #make the program sleep for 1 day

        import time
        time.sleep(86400)  #make it sleep for 1 day (24 hours)

