"""
Составьте программу, которая по номеру дня в году выводит число и месяц
в общепринятой форме (например, 33-й день года - 2 февраля).
"""

NumDay = int(input('add number day'))
m = 0
for mounth in range(1, 13):
    if mounth == 2:
        a = 28
    elif (mounth == 1 or mounth == 3 or mounth == 5 or mounth == 7 or mounth == 8  or mounth == 10  or mounth == 12):
        a = 31
    else:
        a = 30
    m += a
    if (NumDay - m <= 31):
        day = NumDay - m
        if (NumDay > 31):
            mounth += 1
        break

if (mounth < 10):
    print(NumDay, f'-й день года - ', day, '.0', mounth, sep='')
else:
    print(NumDay, '-й день года - ', day, '.', mounth, sep='')
