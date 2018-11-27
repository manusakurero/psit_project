"""Board Game Analyze"""
import csv
def table2018():
    """input file as local"""
    #jame local
    with open(r'D:\OVERFOOL\bgg_db_2018_01.csv') as csvfile:
        data = csv.reader(csvfile)
        table = [row for row in data]
        return table
table2018()
