import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Mailtrap SMTP bilgileri
server = smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525)  # 2525 veya 587 portunu deneyin

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read() # Boşlukları arındırın

server.login('9a85bc02edd1ac', '03e19ab844dfab')

msg = MIMEMultipart()
msg['From'] = 'NeuralNine'
msg['To'] = 'test@example.com'  # Test e-postası alıcısı
msg['Subject'] = 'Just A Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
attachment.close()  # Dosyayı kapatın
encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)
text = msg.as_string()
server.sendmail('mailtesting@neuralnine.com', 'test@example.com', text)

# Bağlantıyı kapat
server.quit()
