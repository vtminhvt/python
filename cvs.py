import csv

header = ['Full Name', 'Birthday', 'Email', 'Mobile', 'Language']
data = ['Vo Thanh Minh', 1981, 'abc@gmail.com', 'HaNoi', 'Python beginner']

with open('data.csv', 'w', encoding='utf-8') as f:
writer = csv.writer(f)

# write the header
writer.writerow(header)

# write the data
writer.writerow(data)
