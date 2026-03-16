import pandas as pd
import time

time.sleep(3)

url = "https://www.sports-reference.com/cbb/schools/"
df = pd.read_html(url)[0]

df.to_csv("stats/cbb_schools.csv", index=False)