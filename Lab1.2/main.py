from matplotlib import pyplot
from openpyxl import load_workbook


wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

def getvalue(x):
     return x.value
#Получам года
years =  list(map(getvalue, sheet['A'][1:]))
# Получаем темпереатру
temp = list(map(getvalue, sheet['C'][1:]))

act = list(map(getvalue, sheet['D'][1:]))

pyplot.xlabel('Годы')
pyplot.ylabel('Температура/Активность Солнца')
pyplot.legend(loc='upper left')

pyplot.plot(years, temp, label="Температура")
pyplot.plot(years, act, label="Активность солнца")

pyplot.show()
