import pandas as pd
onlinesession_hours=[2,4,6,7,1]
sleep_hours=[3,7,8,7,9]
working_hours=[4,3,5,2,6]
stu_name=["Charitha","Teju","Jasmine","Saketh","Sathwika"]
screen_time=[3,4,1,2,7]
dict1 = {
    "onlinesession_hours":onlinesession_hours,
    "sleep_hours":sleep_hours,
    "working_hours":working_hours,
    "stu_name":stu_name,
    "screen_time":screen_time
}
print(dict1)
df = pd.DataFrame(dict1)
print(df)
