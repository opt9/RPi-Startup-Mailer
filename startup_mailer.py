#!/usr/bin/env python

import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import yaml

today = datetime.date.today()

# Get Linux IP Address
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
my_ip = 'Your ip is %s' %  ipaddr


# Read Mail Config
with open("config.yml", 'r') as configfile:
    cfg = yaml.load(configfile)

# Send E-Mail
to = cfg['to']
gmail_user = cfg['id']
gmail_password = cfg['pw']
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
