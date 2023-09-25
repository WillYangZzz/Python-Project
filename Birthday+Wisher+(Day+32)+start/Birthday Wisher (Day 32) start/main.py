import smtplib

my_email = "willyang1023@gmail.com"
password = "Black431125698"
connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="zyang431@gmail.com", msg="Hello")
connection.close()
