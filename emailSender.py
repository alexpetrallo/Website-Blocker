import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import time
from datetime import datetime as dt

from string import Template


# print("hello there")
#Send the mail
def add_hours(filename):
    total_hours = 0
    hoursCount = []
    with open(filename, 'r', encoding='utf-8') as hours_file:
        for hours in hours_file:
            hoursCount.append(hours)
        for i in range (0 , len(hoursCount)):
            total_hours = total_hours + int(hoursCount[i])
        return total_hours

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def get_contacts(filename):
    print("get_contacts was called")
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for contact in contacts_file:
            names.append(contact.split()[0])
            emails.append(contact.split()[0])
    print (names, emails)
    return names, emails

# names, emails = get_contacts('contacts.txt')  # read contacts
# message_template = read_template('message.txt')

# return names, emails

# with open('message.txt') as fp:
#     # Create a text/plain message
#     msg = MIMEText(fp.read())
# from email.mime.multipart import MIMEMultipart
def main():
    print("in main")
    names, emails = get_contacts('contacts.txt')
    message_template = read_template('message.txt')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login("websiteblockerbot@gmail.com", "pythonblocker")

    fromAddress = "websiteblockerbot@gmail.com"
    # toAddress = "apetrall@villanova.edu"

    #before you go past this you will have to eddit where the logs are being sent bc i changed the path


    for name, email in zip(names, emails):
        hours = add_hours('work_hours_logged.txt')
        msg = MIMEMultipart()
        name =  name.split("@")[0]
        message = message_template.substitute(PERSON_NAME=name.title(), HOURS_WORKED=hours )
        # message = message_template.substitute(HOURS_WORKED=hours)

        msg['FROM'] = fromAddress
        msg['TO'] = email
        msg['SUBJECT'] = "your productivity from today"
        # body = "new test for other stuff of an email, dont forget to make it message later"
        msg.attach(MIMEText(message, 'plain'))

        server.send_message(msg)

        del msg
        ##later delete the stuff on logged hours file so that it a new day
        ##do it the same way as free time does to blocked sites in host file

    server.quit()
        # text = msg.as_string()



    # body = "Hey Jos, just a quick flex that I can spam the fuck outta people's emails now bc this was sent w python!" # The /n separates the message from the headers
    # server.sendmail("apetrallo@gmail.com", "apetrall@villanova.edu", text)
    # s.quit()
if __name__ == '__main__': #and dt.now() == dt.now():
    main()

# server.quit()
