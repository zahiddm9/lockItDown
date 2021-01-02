from setupCalender import getCalService
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']

def APICalendar(uInput):
    ARRAY = sorting(uInput)
    
    today = datetime.datetime.now().isoformat()
    Calendar = getCalService()
    
    for singleString in ARRAY:
        events_result = Calendar.events().list(calendarId = 'primary', singleEvents = True, timeMin = str(today)[0:11] + '00:00:00Z', orderBy = 'startTime').execute()
        events = events_result.get('items', [])
        
        amount = len (events)
        
        
        TIME = datetime.time(7,0,0)
        temp = datetime.time(7,0,0)
        for event in events:
            temp=TIME
            hourStart = event['start'].get('dateTime', event['start'].get('date'))[11:13]
            #minuteStart = event['start'].get('dateTime', event['start'].get('date'))[14:16]
            
            hourEnd = event['end'].get('dateTime', event['end'].get('date'))[11:13]
            minuteEnd = event['end'].get('dateTime', event['end'].get('date'))[14:16]
            
            if int(singleString[-1]) == 1:
               num = 3
            elif int(singleString[-1]) == 2:
                num = 2
            else:
                num = 1
            
            count = 0
            hourDiff = int(hourEnd) - int(hourStart)
            for i in range(num+1):
                if (int(hourStart) == (temp.hour + i)):
                    TIME = datetime.time(TIME.hour + i + hourDiff,int(minuteEnd) , 0)
                    break
                
        ENDTIME = TIME
        if int(singleString[-1]) == 1:
            ENDTIME = datetime.time(TIME.hour + 3, TIME.minute, 0)
        elif int(singleString[-1]) == 2:
            ENDTIME = datetime.time(TIME.hour + 2, TIME.minute, 0)
        else:
            ENDTIME = datetime.time(TIME.hour + 1, TIME.minute, 0)

        string = singleString.split("|")
        sendToCalendar = {
            'summary' : string[0],
            'description' : string[1],
            'start': {
                'timeZone' : 'America/Toronto',
                'dateTime' : str(today)[0:11] + str(TIME)
            },
            'end' : {
                'timeZone' : 'America/Toronto',
                'dateTime' : str(today)[0:11] + str(ENDTIME)
                
            },
        }
        Calendar.events().insert(calendarId='primary', body=sendToCalendar).execute()

def sorting(USER_STORAGE):
    newList=[]
    Prio1 = 0
    Prio2 = 0
    Prio3 = 0
    
    for i in range(0, len(USER_STORAGE)):
        key = USER_STORAGE[i]
        j = i-1
        while j >= 0 and int(key[-1]) < int(USER_STORAGE[j][-1]):
            USER_STORAGE[j+1] = USER_STORAGE[j]
            j -= 1
        USER_STORAGE[j+1] = key

    #Gets length of each prio
    for i in USER_STORAGE:
        if (int(i[-1]) == 1):               
            Prio1 += 1

    for j in USER_STORAGE:
        if (int(j[-1]) == 2):
            Prio2 += 1

    for k in USER_STORAGE:
        if (int(k[-1]) == 3):
            Prio3 += 1

    #SORTS ALL OF PRIO1   
    for l in range(0,Prio1):
        if (USER_STORAGE[l].find("Academic Work",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(0,Prio1):
        if (USER_STORAGE[l].find("Career",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(0,Prio1):
        if (USER_STORAGE[l].find("Errands",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(0,Prio1):
        if (USER_STORAGE[l].find("Fitness",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(0,Prio1):
        if (USER_STORAGE[l].find("Extracurricular",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(0,Prio1):
        if (USER_STORAGE[l].find("Leisure",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    #SORTS ALL OF PRIO2
    for l in range(Prio1,Prio1 + Prio2):
        if (USER_STORAGE[l].find("Academic Work",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(Prio1,Prio1 + Prio2):
        if (USER_STORAGE[l].find("Career",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(Prio1,Prio1 + Prio2):
        if (USER_STORAGE[l].find("Errands",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(Prio1, Prio1 + Prio2):
        if (USER_STORAGE[l].find("Fitness",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(Prio1,Prio1 + Prio2):
        if (USER_STORAGE[l].find("Extracurricular",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(Prio1,Prio1 + Prio2):
        if (USER_STORAGE[l].find("Leisure",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    #SORTS ALL OF PRIO3
    for l in range(Prio1 + Prio2, Prio1 + Prio2 + Prio3):
        if (USER_STORAGE[l].find("Academic Work",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(Prio1 + Prio2, Prio1 + Prio2 + Prio3):
        if (USER_STORAGE[l].find("Career",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(Prio1 + Prio2, Prio1 + Prio2 + Prio3):
        if (USER_STORAGE[l].find("Errands",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(Prio1 + Prio2, Prio1 + Prio2 + Prio3):
        if (USER_STORAGE[l].find("Fitness",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(Prio1 + Prio2, Prio1 + Prio2 + Prio3):
        if (USER_STORAGE[l].find("Extracurricular",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    for l in range(Prio1 + Prio2, Prio1 + Prio2 + Prio3):
        if (USER_STORAGE[l].find("Leisure",0,100)!=-1):
            newList.append(USER_STORAGE[l])

    return newList
