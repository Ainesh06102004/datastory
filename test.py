import pandas as pd
import statistics
import plotly.express as px
import plotly.graph_objects as go
import csv
with open("savings_data_final.csv") as f:
    read = csv.reader(f)
    savingsdata = list(read)
savingsdata.pop(0)
    
df = pd.read_csv("savings_data_final.csv")

fig = px.scatter(df, y = "quant_saved", color = "rem_any")
#fig.show()

remsent = 0

for i in savingsdata:
    if(int(i[3]) == 1 ):
        remsent += 1

totalpeople = len(savingsdata)
remnotsent = totalpeople - remsent

fig2 = go.Figure(go.Bar(x = ["reminded", "not reminded"], y = [remsent, remnotsent]))

#fig2.show()

moneysaved = []

for i in savingsdata:
    moneysaved.append(float(i[0]))

meantotal = statistics.mean(moneysaved)
mediantotal = statistics.median(moneysaved)
modetotal = statistics.mode(moneysaved)

print(meantotal,mediantotal,modetotal)
