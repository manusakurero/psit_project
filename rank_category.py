""" category of board games """
from data_2018 import table2018
import matplotlib.pyplot as plt
def category():
    """ category rank """
    table_2018 = table2018()
    cate = []
    for i in range(1, len(table_2018)):
        catesplit = table_2018[i][17].split(', ')
        cate.extend(catesplit)
    set_cate = set(cate)
    cate_bg = [[i, cate.count(i)] for i in set_cate]
    return cate_bg

def plot_cate():
    """
    plot graph by cate_bg
    1 - 10 rank
    """
    cate_rank = category()
    cate_rank.sort(key=lambda kv:int(kv[1]))
    cate_rank.reverse()
    cate_10 = cate_rank[:10]
    print(cate_10)
    label = [i[0] for i in cate_10]
    val = [i[1] for i in cate_10]
    plt.bar(label, val)
    plt.show()
plot_cate()
