import datetime as dt

# Get Start and End time for cloudwatch query - epoch
def time_in_query(seconds):
    current_date_and_time = round(dt.datetime.now().timestamp())
    rem_x_seconds = round(dt.datetime.now().timestamp() - seconds)
    return (current_date_and_time, rem_x_seconds)
