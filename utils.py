class TimeInSeconds:
    def toInt(strTime):
        strHrs, strMins, strSecs = strTime.split(":")
        intHrs = int(strHrs) * 3600
        intMins = int(strMins) * 60
        intSecs = int(strSecs)
        intTime = intHrs + intMins + intSecs
        return intTime

    def fromInt(intTime):
        intHrs = int(intTime // 3600)
        intMins = int((intTime % 3600) // 60)
        intSecs = int((intTime % 3600 % 60))
        strTime = f"{intHrs}:{intMins :02}"
        return strTime
