time = int(input('Введите Duration: '))
day = 0
hours = 0
minutes = 0
second = 0
if time // 86400:
    day = time // 86400
    hours = time % 86400 // 3600
    minutes = time % 86400 % 3600 // 60
    second = time % 86400 % 3600 % 60
    print(day, 'Day', hours, 'Hours', minutes, 'Minutes', second, 'Second')
elif time // 3600:
    hours = time // 3600
    minutes = time % 3600 // 60
    second = time % 3600 % 60
    print(hours, 'Hours', minutes, 'Minutes', second, 'Second')
elif time // 60:
    minutes = time // 60
    second = time % 3600 % 60
    print(minutes, 'Minutes', second, 'Second')
else:
    second = time
    print(second, ' Second')