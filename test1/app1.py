import os
import time
import datetime
import csv

curr_path = os.getcwd()
curr_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
row_list = [["SNo", "Name", "Subject"],
              [1, "Ash Ketchum", "English"],
              [2, "Gary Oak", "Mathematics"],
              [3, "Brock Lesner", "Physics"]]

print(1, curr_path)
print(2, curr_time)

env_var1 = os.environ.get('ENV_VAR1', 'Unknown')
print(3, env_var1)

env_var2 = os.environ.get('ENV_VAR2', 'Unknown')
print(4, env_var2)

env_var3 = os.environ.get('ENV_VAR3', 'Unknown')
print(5, env_var3)

#create directory
if not os.path.exists(f"/root/{curr_time}"):
    os.makedirs(f"/root/{curr_time}")

#time.sleep(2)

#with open(f"{curr_path}/{curr_time}.csv","w",newline="") as file:
with open(f"/root/{curr_time}/{curr_time}.csv","w",newline="") as file:
     writer = csv.writer(file)
     writer.writerows(row_list)

print(6, 'Sleep 300s')

time.sleep(120)

print(7, 'Complete')

