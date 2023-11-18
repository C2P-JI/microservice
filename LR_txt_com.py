import csv
import time

while True:
    with open("comm.txt", 'r+') as file:
        line = file.readline()  # Read the first line
        if line:  # Check if there is content in the line
            print(f"Read line: {line.strip()}")
            data = line.split(',') #seperate the line with ',' in order to upload to a csv
            format_data = [data[0], data[1]] + [round(float(value), 2) for value in data[2:]]

            with open("food_log.csv", 'a', newline='') as csv_file:
                csv_write = csv.writer(csv_file)
                csv_write.writerow(data)

            # Clear the file after reading the line
            file.truncate(0)
            print("File cleared.")
    time.sleep(2)  # Wait for 2 seconds before checking again)