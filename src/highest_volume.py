from datetime import datetime


def highest_volume_date(volume, days):
    highest_volume = [0, 0]

    for i in range(days, len(volume)):
        if volume[i][1] > highest_volume[1]:
            highest_volume[1] = volume[i][1]
            highest_volume[0] = datetime.utcfromtimestamp(volume[i][0]/1000).strftime("%d-%m-%Y")

    return highest_volume
