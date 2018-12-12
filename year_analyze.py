"""Year analyze"""
from data_2018 import table2018
import matplotlib.pyplot as plt
def year_analyze():
    """Sort by year with the most boardgame making"""
    table_2018 = table2018()
    #table_2018[0] is type of datas
    #table_2018[row][column] use loop run index
    #ดึงปีทุกตัวออกมาเก็บใน year
    #keep all year in data_2018 to years
    years = [int(table_2018[i][9]) for i in range(1, len(table_2018))]
    #สร้าง set ของ year
    #create set of year
    set_years = set(years)
    #นับปีว่าปีนี้เกิด broadgame จำนวนเท่าไร
    #how many broadgame make in this year?
    years_bg = [[i, years.count(i)] for i in set_years]
    return years_bg[::]

def plot_years():
    """
    plot graph by year_bg
    1987-2017; 30 years
    """
    year_ana = year_analyze()
    year_ana.sort(key=lambda kv:int(kv[0]))
    year_thridty = year_ana[len(year_ana)-32:len(year_ana)-1]
    print(year_thridty)
    label2 = [year[0] for year in year_thridty]
    val = [year[1] for year in year_thridty]
    plt.bar(label2, val)
    plt.show()

plot_years()
