import os
import csv

date = []
pnl = []

totalamount = 0
monthlyaverage = 0
monthlylist = []
monthlysum = 0.00
avg = 0

file = "/Users/stevenovis/Desktop/budget_data.csv"

with open(file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        date.append(row[0])
        pnl.append(float(row[1]))

    for i in range(0, len(pnl)):
        totalamount = float(pnl[i]) + totalamount

    for j in range(1, len(pnl)):
        monthlyaverage = float(pnl[j]) - float(pnl[j - 1])
        monthlylist.append(monthlyaverage)
    for k in range(0, len(monthlylist)):
        monthlysum += monthlylist[k]
        avg = monthlysum / len(pnl)

    for l in range(0, len(pnl)):
        if pnl[l] == max(pnl):
            datemax = date[l]
            pnlmax = pnl[l]
        if pnl[l] == min(pnl):
            datemin = date[l]
            pnlmin = pnl[l]

    print('Financial Analysis')
    print('______________________________')
    print('Total Months = ' + str(len(date)))
    print('Total = ' + str(totalamount))
    print('Average Monthly Change = ' + str(round(avg, 2)))
    print("The Lowest PNL was on " + datemax + ' in the amount of ' + str(pnlmax))
    print("The Lowest PNL was on " + datemin + ' in the amount of ' + str(pnlmin))


f = open('/Users/stevenovis/Desktop/python-challenge/PyBank/PyBankoutput.txt','w')
f.write('Financial Analysis\n')
f.write('______________________________\n')
f.write('Total Months = ' + str(len(date)) + '\n')
f.write('Total = ' + str(totalamount)+'\n')
f.write('Average Monthly Change = ' + str(round(avg, 2))+'\n')
f.write("The Lowest PNL was on " + datemax + ' in the amount of ' + str(pnlmax)+'\n')
f.write("The Lowest PNL was on " + datemin + ' in the amount of ' + str(pnlmin)+'\n')

f.close()

