def send_mail( message, title):
    print "Sending mail..........."
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    gmailUser = 'jason879@ymail.com'
    gmailPassword = 'How12345'
    recipient = 'tonywang16@me.com'

    msg = MIMEMultipart()
    msg['From'] = gmailUser
    msg['To'] = recipient
    msg['Subject'] = title
    msg.attach(MIMEText(message))

    mailServer = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmailUser, gmailPassword)
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    mailServer.close()
    print "Mail sent"

send_mail("2  2 message body", "Scraper Test222")