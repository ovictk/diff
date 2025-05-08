import random
import json
import os

for i in range(10):
    dataArray = []
    rand = random.random()

    if rand < 0.6:
        dataArray.append("y")
    else:
        dataArray.append("o")

    rand = random.random()

    if rand < 0.1:
        dataArray.append("p")
    else:
        dataArray.append("r")

    if dataArray[0] == "y" and dataArray[1] == "p":
        rand = random.random()

        if rand > 0.7:
            dataArray.append("Ap")
        else:
            dataArray.append("An")

    elif dataArray[0] == "y" and dataArray[1] == "r":
        rand = random.random()

        if rand > 0.05:
            dataArray.append("Ap")
        else:
            dataArray.append("An")

    elif dataArray[0] == "o" and dataArray[1] == "p":
        rand = random.random()

        if rand > 0.98:
            dataArray.append("Ap")
        else:
            dataArray.append("An")

    else:
        rand = random.random()

        if rand > 0.2:
            dataArray.append("Ap")
        else:
            dataArray.append("An")

    results_file = "results.json"

    if os.path.exists(results_file):
      with open(results_file, "r") as file:
        try:
          results = json.load(file)
        except json.JSONDecodeError:
          results = []
    else:
      results = []

    results.append(dataArray)

    with open(results_file, "w") as file:
        json.dump(results, file, indent=2)
