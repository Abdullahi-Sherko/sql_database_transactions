from database_connection import database_transactions
from send_email import send_email

data = database_transactions('127.0.0.1', 'TEST')

send_email(data)