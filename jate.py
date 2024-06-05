import pandas as pd
import datetime
from holidays import Holidays

# Constants of the Jalendar system
DAYS_IN_YEAR = 1461
MINUTES_IN_YEAR = 525960
MINUTES_IN_DAY = 360
JON_BIRTH = "1999-11-06 11:15:00"
JON_BIRTH_PD = pd.to_datetime(JON_BIRTH)
DAYS_OF_JEEK = ["Jonsday", "Jewsday", "Jednesday", "Jursday", "Jiday", "Jaturday", "Jalday", "Jarday", "Jinday", "Junday"]

class Jate:
    # Return Jon Weekday, Jon Week, Jon Day, Jon Year, Jon Minute, and Jon Second
    # Return: Array of strings
    def getJate(self, irlTime):
        irlTimePD = pd.to_datetime(irlTime)

        # Get minutes since start of Jalendar to base all dates from
        minutesSinceBirth = pd.Timedelta(irlTimePD - JON_BIRTH_PD) / pd.Timedelta(minutes=1)

        # Current Jon Year equals the minutes since JON_BIRTH divided by the minutes in a Jon Year
        curJYear = int(minutesSinceBirth / MINUTES_IN_YEAR)
        # Current Jon Day equals the remainder of the JYear division divided by minutes in a Jon Day
        curJDay = int((minutesSinceBirth % MINUTES_IN_YEAR) / MINUTES_IN_DAY)
        # Current Jon Minute equals the remainder of the JDay division
        curJMin = int((minutesSinceBirth % MINUTES_IN_YEAR) % MINUTES_IN_DAY)
        # Current Jon Second equals normal seconds, since Jon Seconds are not different
        curJSec = irlTimePD.second
        
        # Conditional adds a zero for prettier printing of time
        if curJSec < 10:
            curJSec = "0" + str(curJSec)

        # Current week of the Jalendar 
        curJWeek = int(curJDay / 10)
        # Current day of the Jeek
        curJWeekday = DAYS_OF_JEEK[curJDay % 10]

        checkHoliday = Jate.isHoliday(self, irlTime)

        curJate = [curJWeekday, curJWeek, curJDay, curJYear, curJMin, curJSec, checkHoliday]

        # Stringify curJate for printing
        for x, item in enumerate(curJate):
            curJate[x] = str(item)

        return curJate
    
    def isHoliday(self, irlTime):
        holidays = Holidays()
        curIRLMonth = irlTime.month
        curIRLDay = irlTime.day

        holidayMessage = 0
        if curIRLDay in holidays.holidays[curIRLMonth]:
            holidayMessage = holidays.holidays[curIRLMonth][curIRLDay]

        return holidayMessage
