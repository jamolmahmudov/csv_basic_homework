from csv import reader
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   
   return list(r)[0]
data=open('data.csv')
r=reader(data,delimiter=',')
print(get_first_row(data=r))

# Read the csv file