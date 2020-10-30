import smtplib, ssl
import mysql.connector


def connect_to_email(host,user,password):
    '''
    This function connects to a email acc via smtplib

    :param host: Imap host e.g. Outlook.office365.com
    :type host: str

    :param user: login data e.g. example.email@outlook.com
    :type host: str

    :param host: password for the user
    :type host: str
    '''

    print("test")

def connect_to_database(password,schema,user='root',port='3308',host='127.0.0.1'):
    '''
    This function connects to a email acc via smtplib

    :param: user, password, schema
    :type: str

    :default param: user='root', port='3308',host='127.0.0.1'
    :type: str

    :return
    '''

    cnx = mysql.connector.connect(user=user, password=password,
                                  host=host,
                                  port=port,
                                  database=schema)
    cursor = cnx.cursor()

    return(cnx, cursor)