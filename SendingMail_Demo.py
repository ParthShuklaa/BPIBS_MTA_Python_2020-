'''

Step1: Import smtplib
Step2: OPen Mail Connection (mail port no )
Step3: Login using Username and Password
Step4: Send Mail
Step5: Close Connection
'''

import smtplib
Connection  = smtplib.SMTP("SMTP.gmail.com",587)
Connection.starttls()
Connection.login("manoj989125@gmail.com ","password .....")
Message ="\t Vote on 8th Feb \n Sending mail using Python Script "
Connection.sendmail("manoj989125@gmail.com","sandeeprawat169@gmail.com" , Message)
print("Mailed successfully.... ")
Connection.close()