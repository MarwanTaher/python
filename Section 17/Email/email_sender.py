import smtplib
from email.message import EmailMessage

name1 = 'Mina'
email1=EmailMessage()
email1['from'] = 'Marwan Salah'
email1['to'] = 'mina.morgan@avelabs.com '
email1['subject'] = 'Intro to python workshop feedback form'

name2 = 'Eslam'
email2=EmailMessage()
email2['from'] = 'Marwan Salah'
email2['to'] = 'eslam.ebrahem@avelabs.com '
email2['subject'] = 'Intro to python workshop feedback form'

name3 = 'Khalid'
email3=EmailMessage()
email3['from'] = 'Marwan Salah'
email3['to'] = 'khalid.lotfy@avelabs.com '
email3['subject'] = 'Intro to python workshop feedback form'

email1.set_content('Hey {},\nPlease fill the feedback form: https://forms.gle/1g61ycHdNEaMfAhq8 \n\nSent from a python script'.format(name1))
email2.set_content('Hey {},\nPlease fill the feedback form: https://forms.gle/1g61ycHdNEaMfAhq8 \n\nSent from a python script'.format(name2))
email3.set_content('Hey {},\nPlease fill the feedback form: https://forms.gle/1g61ycHdNEaMfAhq8 \n\nSent from a python script'.format(name3))


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('marwansalahtaher@gmail.com','242651aya')
    smtp.send_message(email1)
    print('Sent to {}!\n'.format(name1))
    smtp.send_message(email2)
    print('Sent to {}!\n'.format(name2))
    smtp.send_message(email3)
    print('Sent to {}!\n'.format(name3))