import pandas as pd
data = pd.read_csv("access.txt")
data.columns = ["IP", "%l", "%u", "date_and_time","GMT","GET","Status_code","Content_code","URL","System_accessed"]
data.to_csv('task_5_final.csv')
