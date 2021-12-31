from datetime import datetime

def highestVolumeDate(volume, days):
    highestVolumeDate = [0, 0]

    for i in range(days, len(volume)):
        if(volume[i][1] > highestVolumeDate[1]):
            highestVolumeDate[1] = volume[i][1]
            highestVolumeDate[0] = datetime.utcfromtimestamp(volume[i][0]/1000).strftime("%d-%m-%Y")

    return highestVolumeDate
