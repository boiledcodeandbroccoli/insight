#!/usr/local/bin/python3
import csv

# Initialize "global" variables
lines = 0
lookups = {}
output = {}

# Open & read products csvs
with open('../input/products.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:

        # Load product_id & department_id into lookups dict for later use
        lookups[row['product_id']] = int(row['department_id'])

        # If output department doesn't exist, initalize sub-dictionary
        if int(row['department_id']) not in output:
            output[int(row['department_id'])] = {'orders':0,'firsts':0}

# Opens and reads all orders
with open('../input/order_products.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Tracks processing position
        lines += 1

        # catches data errors
        try:

            # progress bar at every 50k lines
            if not lines % 50000:
                print("Proccessing at line {}".format(lines))

            # grabs department from lookups dictionary
            department = lookups[row['product_id']]

            # increments the count of department orders
            output[department]['orders'] += 1

            # if first time orders then this increases count
            if row['reordered'] == '0':
                output[department]['firsts'] += 1
        except:

            # if error was found, prints error at this line and continues
            print("Error proccessing line #{}, data: {}".format(lines,row))

# opens an output file with headers
fob = open('../output/report.csv', 'w')
fob.write("department_id,number_of_orders,number_of_first_orders,percentage\n")

# iterates through results in ascending order
for dept,row in sorted(output.items()):

    # skips outputs if departments have no orders
    if row['orders'] > 0:

        # calculates rounded first time order to total order ratio
        percentage = round(float(row['firsts']) / float(row['orders']),2)

        # write to file department and order statistics
        fob.write("{},{},{},{}\n".format(dept,row['orders'],row['firsts'],percentage))

# lets user know that execution is completed
print("processing completed.{} lines total".format(lines))
