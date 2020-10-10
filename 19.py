import datetime
from datetime import datetime

if __name__ == '__main__':
    f = eval(input("Enter starting year: "))
    l = eval(input("Enter ending year: "))
    sunday = 0
    for year in range(f,l):
        for month in range(1,13):
            if datetime(year,month,1).weekday() == 0:
                sunday += 1
    print(sunday)