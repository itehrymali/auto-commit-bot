from datetime import datetime

with open("data.txt", "a") as f:
    f.write(f"Updated on {datetime.now()}\n")
