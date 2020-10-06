# Yasir Mushtaque Id: 1769403
month_list = {
    'January': '1',
    'February': '2',
    'March': '3',
    'April': '4',
    'May': '5',
    'June': '6',
    'July': '7',
    'August': '8',
    'September': '9',
    'October': '10',
    'November': '11',
    'December': '12'
    }

with open('inputDates.txt', 'r') as f:
    with open('parsedDates.txt', 'w') as x:
        for line in f:
            if line == '-1':
                break
            elif '.' in line:
                date_split = line.split(',')
                month_day, year = date_split[0], date_split[1]
                month_split = month_day.split(' ')
                month, day = month_list[month_split[0]], month_split[1]
                print('{}/{}/{}'.format(month, day, year))
