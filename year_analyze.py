"""Year analyze"""
from data_2018 import table2018
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
    print(years_bg[::])
    #print(*year_sorted, sep=" ")
    #print(gb)
    #print(list(gb))
year_analyze()