# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
#print(data.head(20))

# Решение через get_dumnies()
# print(pd.get_dummies(data['whoAmI']))


#print('*'*100)

# Решение через loc[]
data.loc[data['whoAmI'] == 'human', 'whoamI'] = '1'
data.loc[data['whoAmI'] == 'robot', 'whoamI'] = '0'
print(data.whoamI)
