import csv
f1_path = r"C:\Users\Keith\Documents\data1.csv"
f2_path = r"C:\Users\Keith\Documents\data2.csv"
f_out_path = r"C:\Users\Keith\Documents\data3.csv"
data1 = csv.reader(open(f1_path))
data2 = csv.reader(open(f2_path))

for row in data1:
    line = []
    for entry in row:
        line.append(entry)
    print(line)

for row in data2:
    line = []
    for entry in row:
        line.append(entry)
    print(line)

f_out = open(f_out_path, 'w', newline='')
writer = csv.writer(f_out)

data2 = csv.reader(open(f2_path))
data2_list = list(data2)

data1 = csv.reader(open(f1_path))
for row in data1:
    line = row
    for row_match in data2_list:
        if row_match[0] == row[0]:
            if row_match[1] == row[1]:
            #if row_match[60] == row[48]:
                line.append(row_match[2])
                #line.append(row_match[68])
                #line.append(row_match[70])
                #line.append(row_match[71])
                #line.append(row_match[65])
    print(line)
    writer.writerow(line)