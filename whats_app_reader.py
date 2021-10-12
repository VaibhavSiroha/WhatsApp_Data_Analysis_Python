#This file reads whatsapp dump and lists the number of messages sent by each sender
import pandas as pd
from tkinter import * 
import matplotlib.pyplot as plt
file_path = 'chat.txt'

with open(file_path, mode='r', encoding="utf8") as f:
    data = f.readlines()
dataset = data[1:]
cleaned_data = []
for line in dataset:
    if '/' in line and ':' in line and ',' in line and '-' in line:
        date = line.split(",")[0]
        line2 = line[len(date):]
        time = line2.split("-")[0][2:]
        line3 = line2[len(time):]
        name = line3.split(":")[0][4:]
        line4 = line3[len(name):]
        message = line4[6:-1]
        cleaned_data.append([date, time, name, message])

    else:
        new = cleaned_data[-1][-1] + " " + line
        cleaned_data[-1][-1] = new

#print(cleaned_data)
#res = [str(i or None) for i in cleaned_data]
#print(res)
df = pd.DataFrame(cleaned_data, columns = ['Date', 'Time', 'Name', 'Message'])


filter = df["Message"] != ""
dfNew = df[filter]
#df['Message'].replace('', np.nan, inplace=True)
#print(df)
#dfNew.to_excel("output.xlsx")
x=dfNew['Name'].value_counts(ascending=False).plot(kind='bar');
#y=dfNew['Name'].value_counts(ascending=False).plot(kind='pie');
plt.show()
input("")