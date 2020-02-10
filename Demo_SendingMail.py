import smtplib

Connection  = smtplib.SMTP("smtp.gmail.com",587)
Connection.starttls()
Connection.login("pvppdesigner2k19@gmail.com","pvppcoe@2k19")
Message  = " Tommorrow is holiday*      Conditions apply ....(its a joke ... "
Connection.sendmail("pvppdesigner2k19@gmail.com","parth.shukla1989@gmail.com",Message)
Connection.quit()