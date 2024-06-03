import pandas as pd

DAYS_IN_YEAR = 1461
MINUTES_IN_YEAR = 525960
MINUTES_IN_DAY = 360
JON_BIRTH = "1999-11-06 11:15:00"
JON_BIRTH_PD = pd.to_datetime(JON_BIRTH)

class Jate:
    def getJate(self, irlTime):
        irlTimePD = pd.to_datetime(irlTime)

        minutesSinceBirth = pd.Timedelta(irlTimePD - JON_BIRTH_PD) / pd.Timedelta(minutes=1)

        curJYear = str(int(minutesSinceBirth / MINUTES_IN_YEAR))
        curJDay = str(int((minutesSinceBirth % MINUTES_IN_YEAR) / MINUTES_IN_DAY))
        curJMin = str(int((minutesSinceBirth % MINUTES_IN_YEAR) % MINUTES_IN_DAY))
        curJSec = irlTimePD.second
        
        if curJSec < 10:
            curJSec = str("0" + str(curJSec))
        else:
            curJSec = str(curJSec)

        curJate = [curJDay, curJYear, curJMin, curJSec]

        return curJate