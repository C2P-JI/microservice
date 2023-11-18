import csv
import time



while(True):
    #total_sums = {}
    total_calories=0
    total_water=0
    total_protein=0
    total_carbs=0
    total_sugar=0
    total_fiber=0
    total_fat=0
    with open("run_total.txt", 'r+') as txt_file:
        run = txt_file.readline()
        if run:
            txt_file.truncate(0)
            print("Running total.txt")
            with open("food_log.csv", 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                
                # #initialize dictionary sums
                # for header in reader.fieldnames:
                #     total_sums[header] = 0

                for row in reader:
                    total_calories += float(row['calories'])
                    total_water += float(row['water_g'])
                    total_protein += float(row['protein_g'])
                    total_carbs += float(row['carbs_g'])
                    total_sugar += float(row['sugar_g'])
                    total_fiber += float(row['fiber_g'])
                    total_fat += float(row['fat_g'])
                        #total_sums[header] += value

            with open('total.txt', 'w') as outfile:
                outfile.write(f"calories: {total_calories}\n"
                              f"water (g): {total_water}\n"
                              f"protein (g): {total_protein}\n"
                              f"carbs (g): {total_carbs}\n"
                              f"sugar (g): {total_sugar}\n"
                              f"fiber (g): {total_fiber}\n"
                              f"fat (g): {total_fat}")
                # for header, total_sum in total_sums.items():
                #     outfile.write(f"{header}: {total_sum}\n")

            
            print("File cleared")
    time.sleep(2)
