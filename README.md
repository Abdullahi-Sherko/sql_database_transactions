## In this Repo, transactions on a SQL Server database is simply mailed to your Email.


- database server name is local (127.0.0.1)
- Sender is SMTP using your email address: 'yourmail@gmail.com'
- Password of sender email is gmail [App Password](https://support.google.com/accounts/answer/185833?hl=en)
  * SMTP(user= 'yourmail@gmail.com', password= 'App password')
- Reciever emails are saved in emails.txt file.


## sample output:


|-transaction--|---------occur time--------|

|---UPDATE---|-2022/12/29 01:23:39:340-|

|---INSERT----|-2022/12/27 23:23:39:340-|



## run the Repo:

1) git clone repo
2) cd sql_database_transactions/
3) pip install -r requirements.txt
4) python main.py