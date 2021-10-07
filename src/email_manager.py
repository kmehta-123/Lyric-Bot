"""
LOGIN DETAILS
EMAIL: lyricscraper@gmail.com
PASS: lyric$craper11

"""
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


EMAIL_ADDRESS = 'lyricscraper@gmail.com'
EMAIL_PASSWORD = 'lyric$craper11'

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

def send_file(file):
    user_email = input("Enter email: ")

    msg = MIMEMultipart()

    song_title = os.path.basename(file.name).strip('.txt')

    msg['Subject'] = "{} Lyrics".format(song_title)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = user_email

    attachment = open(file.name, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', 'attachment; filename= %s' % file.name)

    msg.attach(p)

    smtp.send_message(msg)

    print('Lyrics sent! Check your email')

    return True

def quit():
    smtp.quit()

