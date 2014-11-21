#!/usr/bin/env python
def days(year, month):
    if month in (4, 6, 9, 11): return 30
    elif month in (1, 3, 5, 7, 8, 10, 12): return 31
    elif year % 400 == 0 or (year % 100 != 0 and year % 4 == 0): return 29
    return 28

count = 0
today = 0
for year in range(1900, 2001):
    for month in range(1, 13):
        for day in range(1, days(year, month) + 1):
            if year > 1900 and day == 1 and today == 6:
                count += 1
            today = (today + 1) % 7

print(count)
