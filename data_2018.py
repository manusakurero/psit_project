"""Data of board game 2018"""
import csv
def table2018():
    """input file as local"""
    #where is your csv file
    local_file = 'D:\\OVERFOOL\\bgg_db_2018_01.csv'
    #local = r'D:\OVERFOOL\bgg_db_2018_01.csv'
    with open(local_file, "r", encoding='latin-1') as csvfile:
        data = csv.reader(csvfile)
        table = [row for row in data]
        return table
