import json
import random
from collections import defaultdict

# young is 0 and old is 1
# poor is 0 and rich is 1
# apple is 0 and android 1

def predictPhone (inputAge, inputWealth):

    # 1.
    # Laden der Trainingsdaten
    results_file = "results.json"
    loaded_data = []

    try:
        with open(results_file, "r") as file:
            loaded_data = json.load(file)

    except FileNotFoundError:
        print(f"Fehler: Datei '{results_file}' nicht gefunden.")
        exit()

    # 2.
    # Zählen der Haufigkeiten

    #2.1 Initialisierung der Zähler
    counts_phone_given_age_wealth = {}
    counts_age_wealth = {}
    counts_age = {}
    counts_wealth = {}
    data_count = 0

    #2.2 Datenpunkte durchlaufen und Zähler inkrementieren
    for dataArray in loaded_data:
        age = dataArray[0]
        wealth = dataArray[1]
        phone = dataArray[2]

        data_count += 1

        counts_age[age] = counts_age.get(age, 0) + 1

        counts_wealth[wealth] = counts_wealth.get(wealth, 0) + 1

        if age not in counts_age_wealth:
            counts_age_wealth[age] = {}
        counts_age_wealth[age][wealth] = counts_age_wealth[age].get(wealth, 0) + 1

        if age not in counts_phone_given_age_wealth:
            counts_phone_given_age_wealth[age] = {}
        if wealth not in counts_phone_given_age_wealth[age]:
             counts_phone_given_age_wealth[age][wealth] = {}
        counts_phone_given_age_wealth[age][wealth][phone] = counts_phone_given_age_wealth[age][wealth].get(phone, 0) + 1

    # 3.
    # Berechnung der Wahrscheinlichkeiten

    learned_probabilities = {}

    # 3.1 Berechnung P(Age)
    learned_probabilities['P(Age)'] = {}
    for age in [0, 1]:
        count = counts_age.get(age, 0)
        learned_probabilities['P(Age)'][age] = count / data_count if data_count > 0 else 0

    # 3.2 Berechnung P(Wealth)
    learned_probabilities['P(Wealth)'] = {}
    for wealth in [0, 1]:
        count = counts_wealth.get(wealth, 0)
        learned_probabilities['P(Wealth)'][wealth] = count / data_count if data_count > 0 else 0

    # 3.3 Berechnung P(Phone | Age, Wealth)
    learned_probabilities['P(Phone | Age, Wealth)'] = {}
    for age in [0, 1]:
        learned_probabilities['P(Phone | Age, Wealth)'][age] = {}
        for wealth in [0, 1]:
            total_for_group = counts_age_wealth.get(age, {}).get(wealth, 0)

            learned_probabilities['P(Phone | Age, Wealth)'][age][wealth] = {}
            for phone in [0, 1]:
                count = counts_phone_given_age_wealth.get(age, {}).get(wealth, {}).get(phone, 0)
                learned_probabilities['P(Phone | Age, Wealth)'][age][wealth][phone] = count / total_for_group if total_for_group > 0 else 0

    # 4.
    # Ausgabe der Handy wahl basierend auf inputAge und inputWealth

    probs_for_this_group = learned_probabilities['P(Phone | Age, Wealth)'][inputAge][inputWealth]

    prob_apple = probs_for_this_group.get(0, 0)
    prob_android = probs_for_this_group.get(1, 0)

    random_number = random.random()

    phone = ''
    if random_number > prob_android:
        phone = 'apple'
    elif random_number <= prob_android:
        phone = 'android'

    return phone