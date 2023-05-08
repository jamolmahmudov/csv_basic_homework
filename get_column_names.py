from csv import reader
#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """


    return (list(r)[0])
data=open('data.csv')
r=reader(data,delimiter=',')
print(get_column_names(data=r))
# Read the csv file