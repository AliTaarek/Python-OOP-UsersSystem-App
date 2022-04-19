import datetime


def check_date(date):
    date_arr = date.split("-")
    try:
        datetime.datetime(int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))
        return True
    except Exception as e:
        return False


def date_compare(start, end):
    start_date = start.split("-")
    end_date = end.split("-")
    return datetime.date(int(start_date[0]), int(start_date[1]), int(start_date[2])) < \
        datetime.date(int(end_date[0]), int(end_date[1]), int(end_date[2]))