import yagmail
from convert_df_to_html import convert_to_html
from os.path import exists
def send_email(data):
    if exists('emails.txt'):
        with open('emails.txt', 'r') as f:
            email_list = f.readlines()
    else:
        exit('Failed. Email list file was not found.')     
    email_pass = input('enter email password -> ')
    try:
        yag = yagmail.SMTP(user='kurdataland@gmail.com', password= email_pass)
        yag.send(to=email_list , subject='datbase transactions', contents=convert_to_html(data))
        print("Done. Email sent successfully.")
    except:
        print("Failed. Email was not sent.")

