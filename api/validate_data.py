import json


def validateData ():
  # 1.
  # Laden der Trainingsdaten
  results_file = "results.json"
  loaded_data = []

  try:
      with open(results_file, "r") as file:
          loaded_data = json.load(file)
      print(f"Erfolgreich {len(loaded_data)} Datenpunkte geladen.")

  except FileNotFoundError:
      print(f"Fehler: Datei '{results_file}' nicht gefunden.")
      print("Bitte führe zuerst 'generate_data.py' aus, um die Daten zu erstellen.")
      exit()

  for i, dataArray in enumerate(loaded_data):
      if not isinstance(dataArray, (list, tuple)) or len(dataArray) != 3:
          raise ValueError(f"Fehler im Datensatz {i}: Datenformat ist nicht korrekt. Erwartet Liste oder Tuple mit 3 Elementen, aber {type(dataArray).__name__} mit Länge {len(dataArray) if isinstance(dataArray, (list, tuple)) else 'unbekannt'} gefunden.")

      age = dataArray[0]
      wealth = dataArray[1]
      phone = dataArray[2]

      if not age in [0, 1]:
          raise ValueError(f"Fehler im Datensatz {i}: Alter ({age}) ist nicht korrekt. Erwartet 0 oder 1.")

      if not wealth in [0, 1]:
          raise ValueError(f"Fehler im Datensatz {i}: Vermoegen ({wealth}) ist nicht korrekt. Erwartet 0 oder 1.")

      if not phone in [0, 1]:
          raise ValueError(f"Fehler im Datensatz {i}: Handy ({phone}) ist nicht korrekt. Erwartet 0 oder 1.")

  print("Datenformat ist korrekt.")