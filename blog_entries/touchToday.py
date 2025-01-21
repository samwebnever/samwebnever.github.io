from datetime import datetime
date = datetime.today().strftime('%Y%m%d')
f = open(f"{date}.txt", "a")
f.close()