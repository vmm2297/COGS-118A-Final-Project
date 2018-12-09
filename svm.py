import numpy as np
import csv

#Import Datasets
#1. carPrice
with open('./datasets/carPrice/car.data.csv', 'rb') as csvfile:

    dataReader = csv.reader(csvfile, delimeter = ',')
    for row in dataReader:
        print(row)
