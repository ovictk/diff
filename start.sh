#!/bin/bash

# Beende das Skript sofort, wenn ein Befehl fehlschlägt
set -e

echo "Starte API..."
cd api || { echo "Fehler: Verzeichnis 'api' nicht gefunden."; exit 1; }
python api_app.py &
API_PID=$!
echo "API im Hintergrund gestartet (PID: $API_PID)"

cd ../ || { echo "Fehler: Konnte nicht aus 'api' zurückwechseln."; exit 1; }

echo "Starte Frontend..."
cd frontend || { echo "Fehler: Verzeichnis 'frontend' nicht gefunden."; exit 1; }
npm run dev &
FRONTEND_PID=$!
echo "Frontend im Hintergrund gestartet (PID: $FRONTEND_PID)"

cd ../ || { echo "Fehler: Konnte nicht aus 'frontend' zurückwechseln."; exit 1; }

echo "--------------------------------------------------"
echo "API und Frontend laufen jetzt im Hintergrund."
echo "API PID: $API_PID"
echo "Frontend PID: $FRONTEND_PID"
echo "--------------------------------------------------"
echo "Um die Prozesse zu stoppen, musst du sie separat beenden (z.B. mit 'kill $API_PID' und 'kill $FRONTEND_PID' in einem anderen Terminal, oder indem du dieses Terminal schließt)."
echo "Drücke ENTER, um das Skript zu beenden (dies beendet NICHT unbedingt die Hintergrundprozesse)."

read -r
echo "Skript beendet."