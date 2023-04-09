'''
I could use some assistance in creating a professional, well commented python script that uses the pandas library.  The script should open an excel file to a specific sheet then extract the data for further transformations using pandas chaining methods.  I'll go into more detail with the transformation methods but can you write a script to start and I'll add more details on the transformations in subsequent messages.

The script should be parameterized where appropriate on things like excel name and location, sheet name, etc.
'''

import pandas as pd

# Open the excel file to a specific sheet
def open_excel(filename, sheetname):
    try:
        df = pd.read_excel(filename, sheetname)
        return df

    except filenotfounderror:
        print("File not found")
    except sheetnotfounderror:
        print("Sheet not found")
        
# Create a function to open an excel file to a specific sheet and return a dataframe
# Document the function using docstrings
# Make the function fault tolerant
def open_excel(filename, sheetname):
    """
    Opens an excel file to a specific sheet and returns a dataframe.
    
    Parameters
    ----------
    filename : str
        The name of the excel file.
    sheetname : str
        The name of the sheet in the excel file.
        
    Returns
    -------
    df : pandas.core.frame.DataFrame
        A pandas dataframe.
    """
    try:
        df = pd.read_excel(filename, sheetname)
        return df

    except filenotfounderror:
        print("File not found")
    except sheetnotfounderror:
        print("Sheet not found")

# Extract the data for further transformations using pandas chaining methods
# Transform the data
# Save the data to a new csv file
def main():
    df = open_excel("filename.xlsx", "sheetname")
    df = df[["column1", "column2", "column3"]]
    # add a new column that's a combination of col1 and col2 and call it col4 the remove col1 and col2
    # use method chaining
    df = df.assign(col4 = df["col1"] + df["col2"])
    .drop(["col1", "col2"], axis=1)
    # add a new column that's a combination of col3 and col4 and call it col5 the remove col3 and col4
    .assign(col5 = df["col3"] + df["col4"])

    # save the data to a new csv file
    df.to_csv("newfilename.csv", index=False)


if __name__ == "__main__":
    main()

# add unit tests
def test_open_excel():
    df = open_excel("filename.xlsx", "sheetname")
    assert df.shape == (5, 3)
    assert df.columns == ["col1", "col2", "col3"]
    
