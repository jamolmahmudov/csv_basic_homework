from csv import reader
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
       
    return len(list(r))

data=open('data.csv')
r=reader(data,delimiter=',')
print(find_number_of_rows(data=r))


# Read the csv file
