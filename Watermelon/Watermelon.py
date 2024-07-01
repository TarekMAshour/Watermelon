import csv

def csvmakedataframe(file_name):
    """
    Creates a dataframe from a csv File
    kwargs*: File Name
    Returns: DataFrame
    """
    data = []
    with open(file_name, 'r') as file:
        headers = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            row = dict(zip(headers, values))
            data.append(row)
    return data

def createdataframe(data):
    """
    Creates a dataframe
    Kwargs*: Listed Data with dictionaries
    Returns: Headers, Rows and Column Indices
    """
    if isinstance(data, list):
        if len(data) == 0:
            raise ValueError("Input list is empty. Cannot create DataFrame.")
        column_indices = {}
        
        headers = list(data[0].keys())
        
        rows = [list(dictionary.values()) for dictionary in data]
        
        for index, header in enumerate(headers):
            column_indices[header] = index
        
        return {'headers': headers, 'rows': rows, 'column_indices': column_indices}
    else:
        raise TypeError(f"Expected a list of dictionaries but got this value: {data}")

def getcolumn(dataframe, column_name):
    """
    Retrieves the values from a specified column in the custom DataFrame-like structure.

    Kwargs*:
        dataframe (dict): The custom data structure with 'headers', 'rows', and 'column_indices'.
        column_name (str): The name of the column to retrieve.

    Returns:
        list: A list containing the values from the specified column.
    """
    if 'column_indices' not in dataframe:
        raise ValueError("Invalid data structure. Missing 'column_indices'.")
    
    column_index = dataframe['column_indices'].get(column_name)
    if column_index is None:
        raise ValueError(f"Column '{column_name}' not found in DataFrame headers.")
    return [row[column_index] for row in dataframe['rows']]