import random
import json
import os

# young is 0 and old is 1
# poor is 0 and rich is 1
# apple is 0 and android 1
results = []

total_cnt = 10

ap_cnt = 0
an_cnt = 0
y_cnt= 0
o_cnt = 0
p_cnt = 0
r_cnt = 0

for i in range(total_cnt):
    dataArray = []
    rand = random.random()

    # young or old
    if rand < 0.6:
        dataArray.append(0)
        y_cnt =+ 1
        
    else:
        dataArray.append(1)
        o_cnt =+ 1

    # poor or rich
    rand = random.random()

    if rand < 0.1:
        dataArray.append(0)
        p_cnt =+ 1
    else:
        dataArray.append(1)
        r_cnt =+ 1

    # apple or android
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
            ap_cnt =+ 1
            dataArray.append(0)
        else:
            an_cnt =+ 1
            dataArray.append(1)

    results_file = "results.json"
    predictions_file = "predictions.json"

    # if os.path.exists(results_file):
    #   with open(results_file, "r") as file:
    #     try:
    #       results = json.load(file)
    #     except json.JSONDecodeError:
    #       results = []
    # else:

    results.append(dataArray)

predictions = {
    "ap": ap_cnt / total_cnt * 100,
    "an": an_cnt / total_cnt * 100,
    "y": y_cnt / total_cnt * 100,
    "o": o_cnt / total_cnt * 100,
    "p": p_cnt / total_cnt * 100,
    "r": r_cnt / total_cnt * 100, 
}

with open(predictions_file, "w") as file:
    json.dump(predictions, file, indent=2)

with open(results_file, "w") as file:
    json.dump(results, file, indent=2)