import random
import smtplib
import tkinter as tk
from tkinter import *

# Generate a random 6-digit OTP
otp = random.randint(100000, 999999)
bg_color = "#ffffff"

# Sender email credentials
sender_email = "mulugetahailegnaw89@gmail.com"
sender_password = "hnthcbobetmnvkge"
server = smtplib.SMTP("smtp.gmail.com", 587)

def send_otp_email(email):
    try:
        server.starttls()
        server.login(sender_email, sender_password)
        message = f"Your OTP is {otp}. Please enter this code to verify your identity."
        server.sendmail(sender_email, email, message)
        print("OTP sent successfully.")
    except:
        print("Error sending OTP email.")
    finally:
        server.quit()


def verify_otp():
    user_otp = otp_entry.get("1.0","end-1c")
    if user_otp.isdigit() and len(user_otp) == 6:
        if int(user_otp) == otp:
            result_label.config(text="OTP verification successful.")
        else:
            result_label.config(text="OTP verification failed. Please try again.")
    else:
        result_label.config(text="Invalid OTP. Please enter a 6-digit code.")

# Create Tkinter GUI
root = tk.Tk()
root.geometry("500x500")
root.title("OTP Verification")
root.configure(bg=bg_color)


email_label = tk.Label(root, text="Enter your email address:")
email_label.place(x=10, y=20)

email_entry = Text(root, width= 25, height= 1, background= bg_color,foreground="#000000",font= ('Sans Serif', 13, 'italic bold'))
email_entry.place(x= 150, y = 20)


otp_button = tk.Button(root, text="Send OTP", command=lambda: send_otp_email(email_entry.get("1.0",END)))
otp_button.place(x=390, y=20)


otp_label = tk.Label(root, text="Enter the OTP sent to your email:")

otp_label.place(x=10, y=70)

otp_entry = Text(root, width= 25, height= 1, background= bg_color,foreground="#000000",font= ('Sans Serif', 13, 'italic bold'))

otp_entry.place(x=190, y=70)

verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)
verify_button.place(x=420, y= 70)

result_label = tk.Label(root, text="")
result_label.place(x=150, y=150)


root.mainloop()