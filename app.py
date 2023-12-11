from flask import Flask, render_template, request, jsonify
import smtplib
import random

app = Flask(__name__)

# Your global OTP variable
otp = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_otp', methods=['POST'])
def generate_otp():
    global otp
    otp = str(random.randint(1000, 9999))
    return jsonify({"otp": otp})

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

if __name__ == '__main__':
    app.run(debug=True)
