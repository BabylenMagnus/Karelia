import pandas as pd
import os


PATH = 'Годовые отчеты об исполнении бюджета'
for file in os.listdir(PATH):
    print(file)
    data = pd.ExcelFile(PATH + '/' + file)
    print(data.parse(0))
