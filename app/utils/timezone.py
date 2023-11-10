from datetime import datetime, timedelta
from pytz import timezone

def convert_to_local_time(utc_dt, local_tz_str='Asia/Kolkata'):
    local_tz = timezone(local_tz_str)
    return utc_dt.replace(tzinfo=timezone('UTC')).astimezone(local_tz)
