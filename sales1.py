import plotly.express as px
import csv
import numpy as np
def getdata(path):
    icecream = []
    colddrinks = []
    with open(path) as f:
        df = csv.DictReader(f)
        for row in df:
            icecream.append(float(row['Marks']))
            colddrinks.append(float(row['Days']))
    return {'x':icecream, 'y':colddrinks}
def find(data):
    corelation = np.corrcoef(data['x'],data['y'])
    print(corelation[0,1])
def setup():
    path1 = 'sales1.csv'
    data = getdata(path1)
    find(data)
setup()
