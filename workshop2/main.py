import gspread
import numpy as np
gc = gspread.service_account(filename='unitydatascience-437115-c234fcff9cc8.json')
sh = gc.open("UnityWorkshop2")
minutes = list(range(1,15))
i = 0
while i <= len(minutes):
    i += 1
    if i == 0:
        continue
    else:
        current_hp = np.random.randint(0, 50)
        sh.sheet1.update(('A' + str(i)), str(i))
        sh.sheet1.update(('B' + str(i)), str(current_hp))
        print(current_hp)