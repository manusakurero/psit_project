"""Data of board game 2018"""
import csv
def table2018():
    """input file as local"""
    with open("bgg_db_2018_01.csv", "r") as csvfile:
        data = csv.reader(csvfile)
        table = [row for row in data]
        return table
