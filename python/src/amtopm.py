def timeConversion(s):
    hours = s [0:2]
    ampm = s [8:10] 

    if int (hours) < 0 or int (hours) > 12:
        raise Exception ('Hours must be between 0 and 12')

    if 'AM' == ampm:
        if '12' == hours:
            hours = '00'
    elif 'PM' == ampm:
        if '12' != hours: # change hours unless it's midday
            hours = str (int (hours) + 12)

    return hours + ':' + s[3:5] + ':' + s[6:8]

if __name__ == '__main__':
    s = '12:03:04PM'

    result = timeConversion(s)

    print (result)