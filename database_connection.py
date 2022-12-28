import sys
import pyodbc
import pandas as pd

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


def flatten_list(lst):
    flatList = []
    for items in lst:
        if type(items) is list:
            for item in items:
                flatList.append(tuple(item))
        else:
            flatList.append(tuple(items))
    return flatList


def database_transactions(server_name, database_name):
    conn = pyodbc.connect(""" 
                              Driver={{SQL Server}};
                              server={0};
                              Database={1};
                              Trusted_Connection=yes;"""
                          .format(server_name, database_name))
    cursor = conn.cursor()
    transactions = ['delete', 'update', 'insert']
    transaction_report = []
    for transaction in transactions:
        data= cursor.execute(f"select [Transaction Name], [Begin time]  from fn_dblog(null, null) where [Transaction Name] = '{transaction}'")
        transaction_report.append(data.fetchall())
    return pd.DataFrame(flatten_list(transaction_report), columns= ['transaction', 'occur time'])
