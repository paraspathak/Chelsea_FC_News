
class Email_Sender:
    def __init__(self):
        self.account_to_send_from = 'chelsea.news.to.your.inbox@gmail.com'  # email to log in using gmail assumed
        self.account_to_send_from_password = 'Pythonisamazing1234'          #password for the email you provided
        self.user_to_send_to = []
    
    @property
    def user_to_send_to(self):
        return self.user_to_send_to
    
    @user_to_send_to.setter
    def user_to_send_to(self, value):
        self.user_to_send_to = value
    
    @user_to_send_to.deleter
    def user_to_send_to(self):
        del self.user_to_send_to

    def send_email(self, msg, title):
        import smtplib
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEText import MIMEText

        #message = MIMEMultipart()                          #uncomment this and below if you want one message to be sent to all of the people in the list
        #message['From'] = self.account_to_send_from        # ie to will include all the people in the list user_to_send_to

        for email in self.user_to_send_to:
            message = MIMEMultipart()                       #uncomment this and below if you want multiple messages to be sent to all of the people in the list
            message['From'] = self.account_to_send_from     # ie one email per person will be sent to all the people in the list user_to_send_to
            message['To'] = email
            message['Subject'] = title
            message.attach(MIMEText(msg))

            mail_server = smtplib.SMTP('smtp.gmail.com', 587)
            mail_server.ehlo()
            mail_server.starttls()
            mail_server.ehlo()
            mail_server.login(self.account_to_send_from,self.account_to_send_from_password)
            mail_server.sendmail(self.account_to_send_from, email, message.as_string())
            mail_server.close()

        print("Mail sent")

""" Test class
email = Email_Sender()
email.user_to_send_to = ['___Insert Email address here___', '___Insert Email address here___']
email.send_email("Class implementation","Single user per email")
"""
