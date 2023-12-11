from tkinter import *
from tkinter import messagebox
import smtplib
import random
import imaplib
import email
from email.header import decode_header

otp = random.randint(1000, 9999)
otp = str(otp)
print("Your OTP is", otp)

def read_emails():
    try:
        email_address = "your_email@gmail.com"
        email_password = "your_password"

        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_address, email_password)
        mail.select("inbox")

        result, data = mail.search(None, "ALL")
        email_ids = data[0].split()

        for email_id in email_ids:
            result, message_data = mail.fetch(email_id, "(RFC822)")
            raw_email = message_data[0][1]
            msg = email.message_from_bytes(raw_email)
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")
            messagebox.showinfo("Email Subject", subject)

        mail.logout()
    except:
        messagebox.showinfo("Read Emails", "An error occurred while reading emails.")

root = Tk()
root.title("Read Emails")
root.geometry("565x450")

read_email_button = Button(root, text="Read Emails", font="ariel 15 bold", bg="black", fg="green2", bd=3, command=read_emails)
read_email_button.place(x=210, y=150)

root.mainloop()
