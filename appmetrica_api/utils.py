import datetime as dt


def get_min_dt(date: dt.date) -> str:
    return dt.datetime.combine(date, dt.time.min).strftime('%Y-%m-%d %H:%M:%S')


def get_max_dt(date: dt.date) -> str:
    return dt.datetime.combine(date, dt.time.max).strftime('%Y-%m-%d %H:%M:%S')
