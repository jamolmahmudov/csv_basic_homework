from csv import reader
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    list=[]
    for i in data:
        list.append(i[1])
    return list
data=open('data.csv')
r=reader(data,delimiter=',')
print(get_first_column(data=r))
    
# Read the csv file