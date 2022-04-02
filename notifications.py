import smtplib

def send_mail(host,ip):
    gmail_user = 'mssd.group2@gmail.com'  
    gmail_password = 'mz6ipfdXLwZqDGA'

    sent_from = gmail_user  
    to = ['mssd.group2@gmail.com']  
    subject = 'note'
    body = """
    The following devices not reacheable
    Host : %s
    IP address : %s
    """ % (host,ip)

    email_text = """
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    return