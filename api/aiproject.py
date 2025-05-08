import random
import json
import os

# young is 0 and old is 1
# poor is 0 and rich is 1
# apple is 0 and android 1
results = []
ap_cnt = 0
an_cnt = 0

for i in range(10):
    dataArray = []
    rand = random.random()

    if rand < 0.6:
        dataArray.append(0)
    else:
        dataArray.append(1)

    rand = random.random()

    if rand < 0.1:
        dataArray.append(0)
    else:
        dataArray.append(1)

    if dataArray[0] == 0 and dataArray[1] == 0:
        rand = random.random()

        if rand > 0.7:
            ap_cnt =+ 1
            dataArray.append(0)
        else:
            an_cnt =+ 1
            dataArray.append(1)

    elif dataArray[0] == 0 and dataArray[1] == 1:
        rand = random.random()

        if rand > 0.05:
            ap_cnt =+ 1
            dataArray.append(0)
        else:
            an_cnt =+ 1
            dataArray.append(1)

    elif dataArray[0] == 1 and dataArray[1] == 0:
        rand = random.random()

        if rand > 0.98:
            ap_cnt =+ 1
            dataArray.append(0)
        else:
            an_cnt =+ 1
            dataArray.append(1)

    else:
        rand = random.random()

        if rand > 0.2:
            dataArray.append(0)
        else:
            dataArray.append(1)

    results_file = "results.json"

    # if os.path.exists(results_file):
    #   with open(results_file, "r") as file:
    #     try:
    #       results = json.load(file)
    #     except json.JSONDecodeError:
    #       results = []
    # else:

    results.append(dataArray)


with open(results_file, "w") as file:
    json.dump(results, file, indent=2)