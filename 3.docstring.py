def readable_timedelta(days):
    """Seperating numbers of days into weeks and day.
      The Function readable_timedelta takes the argument days then finds how many weeks can be found in it
      by dividing the argument by 7 using float and recording the remainder as number of days"""

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
