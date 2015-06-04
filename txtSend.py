import sys, smtplib

def send(usr, pwd, to, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(usr, pwd)  
    server.sendmail(usr, to, msg)  
    server.quit()
        
name = 'KingMak'
SubjectMsg = '--'
args = sys.argv

if len(args) != 5:
    sys.exit('usage: to[email / phone] from[email] password message')

to = args[1]
username = args[2] 
password = args[3]
message = 'From: %s <%s>\nTo: <%s>\nSubject: --\n%s' % (name, username, to, args[4])

try:
    send(username, password, to, message)
    sys.exit('message sent')

except Exception, error:
    sys.exit('message not sent: ' + str(error))
