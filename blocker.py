import time
from datetime import datetime as dt
from datetime import timedelta
import os
from emailSender import main

hosts_temp = "hosts"
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'  #the r is so that you can read the \ not as an escape character
#blank page to redirect to
redirect = '127.0.0.1'

##what i need to  do now is make things more modular and stull call them after the def name()
##gotta add some of those functions to the else statement and put
#append_write stuff somewhere else after teh file is deleted in order to repeat in case the day caries over during work time


filename = 'work_hours_logged.txt'
if os.path.exists(filename):
    append_write = 'a' #a for append my dude
else:
    append_write = 'w' #dubya for wwwwwrite that shit my dude
to_write = open(filename, append_write)

#uncomment
#get the sites

more = True;
while more:
    bad_sites = []
    sitess = input("Enter the url of the site you would like to block (DONE if done, DEFAULT if default): ")
    if (sitess == 'DONE'):
        more = False
    elif (sitess == 'DEFAULT'):
        bad_sites = ['www.facebook.com', 'facebook.com', 'coolmath4kids.com','www.coolmath4kids.com']
        more = False
    else:
        bad_sites.append(sitess)




    #later try to enter one by one, DONE if DONE in an if statement
# bad_sites = ['www.facebook.com', 'www.facebook.com' ,'facebook.com', 'coolmath4kids.com','www.coolmath4kids.com']



#uncomment
working_hours = int(input("How many hours will you be working? "))
to_write.write(str(working_hours) + "\n")
to_write.close()



# working_minutes =  int(input("and minutes? "))
print(dt.now())

#uncomment
start_time =  dt.now()
end_time = dt.now() + timedelta(hours = working_hours)



# + timedelta(hours = working_minutes)



def working_time():
    start_time = dt.now()
    print("Working Time")
    print(start_time)
    with open(hosts_path,'r+') as file:
        content = file.read()
        for site in bad_sites:
            if site in content:
                pass
            else:
                file.write(redirect+' '+site+'\n')


while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, 23, 59) < dt.now() < dt.now() + timedelta(minutes = 1)):
        main()
        os.remove("work_hours_logged.txt")
    if (start_time<end_time):
        working_time()
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in bad_sites):
                    file.write(line)
                file.truncate()
            print("This is now your free time.")
            back_to_work = input("Do you want to get back to work (yes)? ")
            if(back_to_work == 'yes'):
                to_write = open(filename, append_write)
                working_hours = int(input("How many hours will you be working? "))
                to_write.write(str(working_hours) + "\n")
                start_time = dt.now()
                end_time = dt.now() + timedelta(hours = working_hours)
                to_write.close()
                # end_time = dt.now() + timedelta(hours = working_hours)
    time.sleep(30)


# if (dt.now() == 00:00:00.000000


# if (dt(dt.now().year, dt.now().month, dt.now().day, 24, 59) < dt.now() < dt.now() + timedelta(minutes = 1)):
# if True:
#     main()
#find a way to call send email function






#
# while True:
#     #working is 9-5?
#     if (dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22)):
#         print("Working Time")
#         with open(hosts_path,'r+') as file:
#             content = file.read()
#             for site in bad_sites:
#                 if site in content:
#                     pass
#                 else:
#                     file.write(redirect+' '+site+'\n')
#     else:
#         with open(hosts_path, 'r+') as file:
#             content = file.readlines()
#             file.seek(0)
#             for line in content:
#                 if not any(site in line for site in bad_sites):
#                     file.write(line)
#                 file.truncate()
#             print("Free time")
#     time.sleep(5)
#

# siteNum = int(input("How many sites do you want to block? "))
#
# for in range(i, siteNum):
#     website_list = []
#     website = input("Paste the URL of the site you want to block: ")
#     website_list.append(website)
#
# startTime
