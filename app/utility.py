import sys

secs_per_year = (60 * 60 * 24 * 365)
secs_per_day = (60 * 60 * 24)
secs_per_hour = (60 * 60)
secs_per_minute = 60

# Takes a number of seconds and returns a list in the following format:
#    [seconds, minutes, hours, days, years]
# Length of the returned list is variable - if the function is passed '65', [5, 1] will be returned.
def split_seconds(seconds_total):
    seconds = int(float(seconds_total))
    split_time = []
    
    years = seconds / secs_per_year
    if years > 0:
        split_time.insert(0, years)
        seconds = seconds - (years * secs_per_year)
    days = seconds / secs_per_day
    if days > 0:
        split_time.insert(0, days)
        seconds = seconds - (days * secs_per_day)
    hours = seconds / secs_per_hour
    if hours > 0:
        split_time.insert(0, hours)
        seconds = seconds - (hours * secs_per_hour)
    minutes = seconds / secs_per_minute
    if minutes > 0:
        split_time.insert(0, minutes)
        seconds = seconds - (minutes * secs_per_minute)
    split_time.insert(0, seconds)
    return split_time
