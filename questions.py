import csv
import geojson

# Specify the path to your CSV file
csv_file_path = "pdf1.csv"

# Create a list to store the data from the CSV file
arr = []
# Open the CSV file
with open(csv_file_path, newline='') as csvfile:
    # Create a CSV reader
    csv_reader = csv.reader(csvfile)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        arr.append(row[1])


print(arr)
