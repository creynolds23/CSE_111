"""
Author: Conner Reynolds
Purpose: Readn and edit CSV files
Date: 9/12/22
"""

import csv

def main():

    PRODUCT_INDEX = 0
    product_dict = read_dict('products.csv', PRODUCT_INDEX)
    print(product_dict)





def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:

        # use csv module to create reader object
        reader = csv.reader(csv_file)

        # skip first line in the file
        next(reader)

        # Read rows in the CSV file each row
        for row_list in reader:

            if len(row_list) != 0:

                key = row_list[key_column_index]

                # store the data from current row in dict
                dictionary[key] = row_list
    return dictionary



if __name__ == "__main__":
    main()
