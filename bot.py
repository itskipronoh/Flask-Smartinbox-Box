from flask import Flask, request, render_template
from twilio.rest import Client
import smtplib
import random

app = Flask(__name__)

# Your global OTP variable
otp = ""

@app.route('/send_email', methods=['POST'])
def send_email():
    global otp
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        sender = "pythonproject24@gmail.com"
        password = "myzxaqasdfzwpdzy"
        s.login(sender, password)
        s.sendmail(sender, request.form['email'], otp)
        s.quit()
        return "OTP sent to " + request.form['email']
    except Exception as e:
        return "Failed to send OTP via email: " + str(e)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    global otp
    try:
        account_sid = 'AC75cfa95aa7fde813551bc216a9a18977'
        auth_token = '5d37fea024701586bb168228cc603b11'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body='Hello Your Secure Device OTP is - ' + otp,
            from_='19292051587',
            to=request.form['mobile']
        )
        return "OTP sent to " + request.form['mobile']
    except Exception as e:
        return "Failed to send OTP via SMS: " + str(e)

@app.route('/')
def home():
    return render_template('index.html')

# Your OTP generation logic
def generate_otp():
    global otp
    otp = str(random.randint(1000, 9999))

if __name__ == '__main__':
    generate_otp()
    app.run(debug=True)
