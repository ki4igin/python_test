# This is a sample Python script.
from typing import Tuple

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import table
import numpy as np
from matplotlib import pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


data = pd.read_excel('СМ5-31Б_ЛР1_Никулина_ЗЕ_Василенко_ВД.xlsx', index_col=None, skiprows=1)


print(table.get_d(10))

# print(t_table)
# print(data.keys())
#
# print(data.loc[:, 'R2WR, Ом'])
#
# r2wr = data.loc[:, 'R2WR, Ом'].to_numpy()
#
# marks = r2wr
# fig, axis = plt.subplots()
# axis.hist(marks)
# # Displaying the graph
# plt.show()
