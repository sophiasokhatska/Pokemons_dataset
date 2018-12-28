import plotly
import plotly.graph_objs as go
from plotly import tools
import csv
import re

input_file = "E:/pocemon_dataset(kollok 2)/data/pokemon.csv"

def getName(line):
    data = str(re.split(r',', line, maxsplit=2)[1])
    lst = re.findall(r'^(([a-zA-Z]+) ?){1,3}$', data)
    result = str()
    for i in range (len(lst)):
        element = lst[i][0]
        result += (element[0].upper()+element[1:].lower())
        result+=" "
    return result

def getType_1(line):
    data = re.split(r',', line, maxsplit=3)[2]
    element = re.findall(r'^(([a-zA-Z]+) ?){1,3}$', data)[0][0]
    result = element[0].upper() + element[1:].lower()
    return result

def getType_2(line):
    data = re.split(r',', line, maxsplit=4)[3]
    element = re.findall(r'^(([a-zA-Z]+) ?){1,3}$', data)
    if element==[]:
        return None
    element = element[0][0]
    return element[0].upper() + element[1:].lower()

def getHP(line):
    element = re.split(r',', line, maxsplit=5)[4]
    result = float((re.findall(r'\d+[,.]?\d*', element)[0][0]).replace(",", "."))
    return result

try:
    with open(input_file, encoding="utf-8", mode='r') as file:
       file.readline()
       line_number = 1
       for line in file:
           print(line)
           print(getName(line))
           print(getType_1(line))
           print(getType_2(line))
           print(getHP(line))
           print("\n")
           line_number += 1
except IOError as e:
   print ("I/O error({0}): {1}".format(e.errno, e.strerror))
except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number))

# 3 стовпчикові діаграми: имя - тип 1, имя - тип 2, имя- хп, з в ряд