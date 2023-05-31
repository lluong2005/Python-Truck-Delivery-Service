class TimeInSeconds():
    def toInt(strTime):
        strHrs, strMins, strSecs = strTime.split(":")
        intHrs = int(strHrs) * 3600
        intMins = int(strMins) * 60
        intSecs = int(strSecs)
        intTime = intHrs + intMins + intSecs
        return intTime

    def fromInt(intTime):
        intHrs = intTime // 3600
        intMins = (intTime % 3600) // 60
        intSecs = (intTime % 3600 % 60)
        strTime = f"{intHrs :02}:{intMins :02}:{intSecs :02}"
        return strTime
