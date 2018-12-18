""" top 10 owned """
from data_2018 import table2018
import matplotlib.pyplot as plt
def own():
    """ make list of owned """
    table_2018 = table2018()
    owned = [int(table_2018[i][16]) for i in range(1, len(table_2018))]
    name = [table_2018[i][3] for i in range(1, len(table_2018))]
    owned_bg = [[name[i], owned[i]] for i in range(1, len(name))]
    return owned_bg[::]

def plot_owned():
    """ plot graph """
    owned = own()
    owned.sort(key=lambda kv:int(kv[1]))
    owned.reverse()
    own_10 = owned[:10]
    print(own_10)
    label = [i[0] for i in own_10]
    val = [i[1] for i in own_10]
    plt.bar(label, val)
    plt.show()
plot_owned()
