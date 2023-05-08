from csv import reader
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    
   
    return len(list(r)[1])

data=open('data.csv')
r=reader(data,delimiter=',')
print(find_number_of_columns(data=r))

# Read the csv file