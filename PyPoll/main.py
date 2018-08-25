import io
import csv


file = '/Users/stevenovis/Desktop/election_data.csv'

voterid = []
county = []
candidate = []
khan = []
correy = []
li = []
otoole = []

with open(file, newline='') as csvreader:
    csvfile = csv.reader(csvreader)
    csvheader = next(csvfile)


    for row in csvfile:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        total = len(voterid)
        if row[2] == 'Khan':
            khan.append(row[2])
            khan_num = len(khan)
            khan_pct = round(100*(khan_num/total),2)
        elif row[2] == 'Correy':
            correy.append(row[2])
            correy_num = len(correy)
            correy_pct = round(100 * (correy_num / total), 2)
        elif row[2] == 'Li':
            li.append(row[2])
            li_num = len(li)
            li_pct = round(100 * (li_num / total), 2)
        else:
            otoole.append(row[2])
            otoole_num = len(otoole)
            otoole_pct = round(100 * (otoole_num / total), 2)

if khan_pct > correy_pct > li_pct > otoole_pct:
    winner = 'Khan'
elif correy_pct > li_pct > otoole_pct:
    winner = 'Correy'
elif  li_pct > otoole_pct:
    winner = 'Li'
else:
    winner = 'O Toole'

print('Election Results')
print('------------------------------')
print('Total Votes: ' + str(len(voterid)))
print('Khan: ' + str(khan_pct) + '('+str(len(khan))+')' )
print('Correy: ' + str(correy_pct) + '('+str(len(correy))+')' )
print('Li: ' + str(li_pct) + '('+str(len(li))+')' )
print('O Toole: ' + str(otoole_pct) + '('+str(len(otoole))+')' )
print('------------------------------')
print('Winner: ' + winner)


f = open('/Users/stevenovis/Desktop/python-challenge/PyPoll/PyPolloutput.txt','w')
f.write('Election Results\n')
f.write('------------------------------\n')
f.write('Total Votes: ' + str(len(voterid)) + '\n')
f.write('Correy: ' + str(correy_pct) + '('+str(len(correy))+')\n')
f.write('Li: ' + str(li_pct) + '('+str(len(li))+')\n' )
f.write('O Toole: ' + str(otoole_pct) + '('+str(len(otoole))+')\n')
f.write('------------------------------\n')
f.write('Winner: ' + winner +'\n')
f.close()

