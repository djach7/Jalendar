import pandas as pd
import math
from datetime import datetime

DAYS_IN_YEAR = 1461
MINUTES_IN_DAY = 350
JON_BIRTH = "1999-11-06 11:15:00"

class Jate:
    def getJate(self, irlTime):
        irlTimePD = pd.to_datetime(irlTime)
        
        jBirthPD = pd.to_datetime(JON_BIRTH)
        curJYear = int(((irlTimePD - jBirthPD).total_seconds()/60)/525600)
        curYear = int((str(datetime.now().year))[2:])
        
        if curYear < curJYear: 
            lastJBirth = "20" + str(curYear) + "-11-06 11:15:00"
        else:
            lastJBirth = "20" + str(curYear - 1) + "-11-06 11:15:00"

        lastJBirthPD = pd.to_datetime(lastJBirth)

        minutesElapsed = pd.Timedelta(irlTimePD - lastJBirthPD) / pd.Timedelta(minutes = 1)
        secondsElapsed = pd.Timedelta(irlTimePD - lastJBirthPD) / pd.Timedelta(seconds = 1)

        relevantSeconds = secondsElapsed / 60

        curJDaySecondsDay = int(relevantSeconds / MINUTES_IN_DAY)    

        curJDaySecondsMin = int(relevantSeconds % MINUTES_IN_DAY)    

        curJDay = int(minutesElapsed / MINUTES_IN_DAY)

        curJMin = int(minutesElapsed % MINUTES_IN_DAY)

        curJate = str(curJDay) + "/" + str(curJYear) + " " + str(curJMin) + " IJ"

        return curJate


        


    
    

