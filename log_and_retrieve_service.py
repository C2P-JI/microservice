import csv
import time


while(True):
    #store infomation if file read store
    with open("run_service.txt", 'r+') as run_file:
        line = run_file.readline() #read the first line
        if line == "store":
            with open("food_info.txt", 'r+') as food_file: #send variable log into this file as a string seperated by commas
                food_item = food_file.readline()
                print(f"Read line: {food_item.strip()}")
                data = food_item.split(',') 
                #format to send data [name, servings, log]
                format_data = [data[0], data[1]] + [round(float(value), 2) for value in data[2:]]

                with open("food_log.csv", 'a', newline='') as csv_file:
                    csv_write = csv.writer(csv_file)
                    csv_write.writerow(format_data)
                
                food_file.truncate(0) #clear food_info.txt
            run_file.truncate(0) #clear run_file

        #end of storing

        #retrieve total calories, water, protein, carbs, sugar, fiber and fat
        elif line == "get_total":
            run_file.truncate(0)
            total_calories=0
            total_water=0
            total_protein=0
            total_carbs=0
            total_sugar=0
            total_fiber=0
            total_fat=0

            print("Calculating total nutritional values")
            with open("food_log.csv", 'r') as csv_file:
                reader = csv.DictReader(csv_file)

                for row in reader:
                    print(row)
                    total_calories += float(row['calories'])
                    total_water += float(row['water_g'])
                    total_protein += float(row['protein_g'])
                    total_carbs += float(row['carbs_g'])
                    total_sugar += float(row['sugar_g'])
                    total_fiber += float(row['fiber_g'])
                    total_fat += float(row['fat_g'])

            
            with open('total.txt', 'w') as outfile:
                outfile.write(f"\ncalories: {total_calories}\n"
                            f"water (g): {total_water}\n"
                            f"protein (g): {total_protein}\n"
                            f"carbs (g): {total_carbs}\n"
                            f"sugar (g): {total_sugar}\n"
                            f"fiber (g): {total_fiber}\n"
                            f"fat (g): {total_fat}\n")


        
        #end of retrieve_totals


