import logging
from utils import check_time
from models import *
import smtplib, ssl
from celery import Celery
import string
import random
import os

app = Celery('tasks', backend='redis://:ZNY00r5EN0t8FtL90X11DS8FNKJlDL33@redis-19697.c100.us-east-1-4.ec2.cloud'
                              '.redislabs.com:196',
             broker='redis://:ZNY00r5EN0t8FtL90X11DS8FNKJlDL33@redis-19697.c100.us-east-1-4.ec2.cloud.redislabs.com'
                    ':196')


@app.task
def send_mail(user_email):
    result = check_time()
    if result:
        outgoing_server = os.getenv('EMAIL_SERVER')
        port = 465
        sender_email = os.getenv('SENDER_EMAIL')
        receiver_email = user_email
        password = os.getenv('PASSWORD')
        user = SuperUser.get_user(user_email)
        message = '{}, Your task has been created!!!'.format(user.username)

        context = ssl.create_default_context()
        server = smtplib.SMTP(outgoing_server, port)

        try:
            logging.basicConfig(filename='email.log', level=logging.INFO)
            #   server = smtplib.SMTP(outgoing_server,port)
            server.starttls(context=context)
            server.connect(outgoing_server, port)
            logging.info('Logging into server')
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        except Exception as e:
            logging.info(e)
            print(e)
        finally:
            server.quit()
            logging.info('Finished')
    else:
        message = {'error': 'Cannot run at this time'}
        return message


@app.task
def create_user(email):
    logging.basicConfig(filename='user.log', level=logging.INFO)
    logging.info('Starting to generate username')
    username = ''.join(random.choices(string.ascii_lowercase))
    logging.info('username generated')
    logging.info('Starting to generate username')
    password = ''.join(random.choices(string.ascii_lowercase + string.digits))
    logging.info('username generated')
    SuperUser(username=username, password=password, email=email)
    logging.info('User created')


if __name__ == '__main__':
    app.worker_main()
