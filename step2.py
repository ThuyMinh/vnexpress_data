import csv

count = 0;
with open('vnexpress_data.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        count += 1
print(count)
