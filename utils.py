import datetime


def check_time(now=datetime.datetime.now()):
    start_time = datetime.timedelta(hours=1, minutes=00, seconds=00)
    st = datetime.datetime.strptime('01:00:00', '%H:%M:%S')
    end = datetime.datetime.strptime('05:00:00', '%H:%M:%S')
    end_time = datetime.timedelta(hours=5, minutes=00, seconds=00)
    if datetime.datetime.now() > st < end:
        return True
    else:
        return False
