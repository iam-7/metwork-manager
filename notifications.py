import smtplib

def send_mail(host,ip):
    gmail_user = 'guru.5798.r@gmail.com'  
    gmail_password = 'Dominus@5'

    sent_from = gmail_user  
    to = ['guru.5798.r@gmail.com']  
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