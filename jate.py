import pandas as pd

# Constants of the Jalendar system
DAYS_IN_YEAR = 1461
MINUTES_IN_YEAR = 525960
MINUTES_IN_DAY = 360
JON_BIRTH = "1999-11-06 11:15:00"
JON_BIRTH_PD = pd.to_datetime(JON_BIRTH)

class Jate:
    def getJate(self, irlTime):
        irlTimePD = pd.to_datetime(irlTime)

        # Get minutes since start of Jalendar to base all dates from
        minutesSinceBirth = pd.Timedelta(irlTimePD - JON_BIRTH_PD) / pd.Timedelta(minutes=1)

        # Current Jon Year equals the minutes since JON_BIRTH divided by the minutes in a Jon Year
        curJYear = str(int(minutesSinceBirth / MINUTES_IN_YEAR))
        # Current Jon Day equals the remainder of the JYear division divided by minutes in a Jon Day
        curJDay = str(int((minutesSinceBirth % MINUTES_IN_YEAR) / MINUTES_IN_DAY))
        # Current Jon Minute equals the remainder of the JDay division
        curJMin = str(int((minutesSinceBirth % MINUTES_IN_YEAR) % MINUTES_IN_DAY))
        # Current Jon Second equals normal seconds, since Jon Seconds are not different
        curJSec = irlTimePD.second
        
        # Conditional adds a zero for prettier printing of time
        if curJSec < 10:
            curJSec = str("0" + str(curJSec))
        else:
            curJSec = str(curJSec)

        curJate = [curJDay, curJYear, curJMin, curJSec]

        return curJate