#!/data/data/com.termux/files/usr/bin/bash
echo "--- INITIALIZING NETRUNNER CORE ---"
python3 main.py &
ENGINE_PID=$!
echo "> Engine Online (Port 5000) [PID: $ENGINE_PID]"
trap "kill $ENGINE_PID; exit" SIGINT SIGTERM
wait
