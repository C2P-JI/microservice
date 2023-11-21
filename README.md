'LR_service.py' will let user's save the foods they ate into a csv file and return the total nutritional value they consumed in that session. Storing the food items int a csv file also allows the programmer to examine and manipulate the data as they so please.

The script was built on Python 3.12.0. 

Crucial information to run 'LR_service.py' properly
  - 'LR_service.py' must exist in the same directory as main file.
    
  - 'LR_service.py' must be ran in a seperate terminal before running the main file
    
  - 'food_log.csv' must exist in the same directory and contain the following headers in the exact order
    as shown below
    header oder: name,servings,calories,water_g,protein_g,carbs_g,sugar_g,fiber_g,fat_g
    
  - 'run_service.txt' must already exist in the same directory before running any file. The purpose of
    'run_service.txt' is to signal 'log_and_retrive_service.py' what to do.
    
  - 'total.txt' this file will be created if it doesn't already exist. The purpose of this file is
    is to store the total nutritional value calculated from 'food_log.csv'. 
    
  - 'food_info.txt' this file will be created if it doesn't already exist. The purpose of this file
    is to transfer the nutrional information of a food item from the main file to 'food_log.csv'


How the program 
  'LR_service.py' will run in a seperate terminal before running your main application. When 
  running 'LR_service.py' will be reading 'run_service.txt' and waiting for either key phrases
  "log" or "get_total".
******************************************************************************************************
  If "log" is sent to 'run_service.txt' then 'LR_service.py' REQUESTS for the following information in  
  'food_info.txt'
    "{name of food}, {number of servings}, {calories}, {water in grams}, 
      {carbs in grams}, {sugar in grams}, {fiber in grams}, {fat in grams}"
  
  From your main application send the information of the food being logged in the following format 
  to 'food_info.txt'
  
  'LR_service.py' then stores the above information into 'food_log.csv'
******************************************************************************************************
  If "get_total" is sent to 'run_service.txt' then 'LR_service.py' calculates the total amount of 
  calories, water(g), carbs(g), sugar(g), fiber(g), and fat(g) from 'food_log.csv' and sends
  the calculated valeus to 'total.txt' in the following format
                    calories: 94.6
                    water (g): 156.0
                    protein (g): 0.43
                    carbs (g): 25.1
                    sugar (g): 18.9
                    fiber (g): 4.37
                    fat (g): 0.3
  To RECIEVE this information your main application needs to open and read each line from 'total.txt'
******************************************************************************************************
UML sequence Diagram
![image](https://github.com/C2P-JI/microservice/assets/75452230/44fe8d9f-8d2b-4d76-8a69-1bb1a20bcfe5)

    
