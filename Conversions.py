import datetime

#to sql
def datetime_to_sql(date):
    f = '%Y-%m-%d %H:%M:%S'
    return date.strftime(f)

#to datetime
def sql_to_datetime(date):
    f = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.strptime(date, f)
