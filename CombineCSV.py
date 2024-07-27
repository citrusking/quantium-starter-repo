import csv

# find the relevant rows
with (open('data/daily_sales_data_0.csv') as csv0, open('data/daily_sales_data_1.csv') as csv1,
      open('data/daily_sales_data_2.csv') as csv2):
    reader0 = csv.reader(csv0)
    reader1 = csv.reader(csv1)
    reader2 = csv.reader(csv2)

    # create arrays for the rows we will be using
    csv0_rows = []
    for row in reader0:
        if row[0] == "pink morsel":
            csv0_rows.append(row)
    csv1_rows = []
    for row in reader1:
        if row[0] == "pink morsel":
            csv1_rows.append(row)
    csv2_rows = []
    for row in reader2:
        if row[0] == "pink morsel":
            csv2_rows.append(row)

# format data from relevant rows into new csv
with open('data/output_sales_data.csv', 'w', newline='') as csv_out:
    fieldnames = ['sales', 'date', 'region']
    writer = csv.DictWriter(csv_out, fieldnames=fieldnames)

    writer.writeheader()
    for row in csv0_rows:
        writer.writerow({'sales': "${:.2f}".format(float(row[1].replace("$", "")) * float(row[2])),
                         'date': row[3], 'region': row[4]})
    for row in csv1_rows:
        writer.writerow({'sales': "${:.2f}".format(float(row[1].replace("$", "")) * float(row[2])),
                         'date': row[3], 'region': row[4]})
    for row in csv2_rows:
        writer.writerow({'sales': "${:.2f}".format(float(row[1].replace("$", "")) * float(row[2])),
                         'date': row[3], 'region': row[4]})
