import csv
import geojson

# Specify the path to your CSV file
csv_file_path = "stands.csv"

# Create a list to store the data from the CSV file
data = []

# Open the CSV file
with open(csv_file_path, newline='') as csvfile:
    # Create a CSV reader
    csv_reader = csv.reader(csvfile, delimiter=';')

    # Iterate through each row in the CSV file
    for row in csv_reader:
        data.append(row)
#print(data[1][2])


with open("geo_location.geojson") as f:
    gj = geojson.load(f)


#print(len(data[1]))
# for i in range(20):
#     print(len(data[i]))
#     print(data[i])

#print(gj['features'])

for stand_loc in gj['features']:
    stand_prop = stand_loc['properties']
    numero = stand_prop['numero']
    center_point = stand_prop['centerpoint']
    for stand_id in range(len(data)):
        if data[stand_id][0] == numero:
            data[stand_id].append(center_point)

output_csv_file_path = "output_combined.csv"

# Open the CSV file for writing
with open(output_csv_file_path, mode='w', newline='') as csvfile:
    # Create a CSV writer
    csv_writer = csv.writer(csvfile, delimiter=';')

    # Write the header row
    csv_writer.writerow(data[0])

    # Write the data to the CSV file, skipping the header
    for row in data[1:]:
        a = s
        csv_writer.writerow(row)

print("Data has been saved to", output_csv_file_path)
# Now, 'data' contains the data from the CSV file
# You can access individual elements like data[row][column]
