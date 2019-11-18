import pandas as pd
import os
#import matplotlib.pyplot as plt
#from matplotlib import pyplot
import plotly.express as px


'''files=[]
path1 = './datastreams/'
for r,d,f in os.walk(path1):
    for filename in f:
        if 'main.csv' in filename:
            continue
        files.append(os.path.join(r, filename))
'''

files = ['./datastreams/Logitech Logi Circle.csv']

for datafile in files:
    df = pd.read_csv(datafile)
    pktlen = df[df.columns[3]]
    pkttime = df[df.columns[4]]
	
    df = pd.concat([pkttime, pktlen], axis = 1)
    fig = px.line(df, x=df[df.columns[0]], y=df[df.columns[1]],title="Graph of Logitech Logi Circle usage")
    fig.update_layout(
    xaxis_title="Time",
    yaxis_title="Packet Length")
    fig.show()
	

    tips = px.data.tips()
    fig = px.box(tips, y=pktlen, x=pkttime,title="Box of Logitech Logi Circle usage")
    fig.update_layout(
    xaxis_title="Time",
    yaxis_title="Packet Length")
    fig.show()

