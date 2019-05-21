# coding: utf-8

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

#total_website_data += "With &hearts from Paras Pathak"
#print(total_website_data)
print("Last statement emailed is", last_title_emailed)

#------------------------
#third load all the emails from the file
users = ['paraspathak@outlook.com','paraspathak@icloud.com']

#------------------------
#fourth we email the file
import send_email

email = send_email.Email_Sender()
email.user_to_send_to = users
email.send_email(total_website_data, "Chelsea Headlines")

#delete the file so as to prevent further addition
import os
os.remove("./data.csv")