#Send mail through code. (This code works for Gmail only. For others, some changes are to be made)

import smtplib

#Email address of the sender andd reciever
sender = 'sender@gmail.com'
receivers = ['reciever@gmail.com']

#Required for login
email_address = sender
email_pass = 'password here'

#The message (Format should be kept same)
message = '''From: Sender <sender@gmail.com>
To: Reciever <reciever@gmail.com>
Subject: Python SMTP test

This is a test email sent by coding in python.
'''

with smtplib.SMTP('smtp.gmail.com', 587) as smtp: #587 is port number
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_address, email_pass)
        smtp.sendmail(sender, receivers, message)         
        print ('Email sent.')
