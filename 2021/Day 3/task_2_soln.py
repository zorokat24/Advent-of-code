# importing pandas
from pickle import NONE
import pandas as pd
  
# read text file into pandas DataFrame
df = pd.read_csv(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 3\input_3.txt", header = None, names = ['binary'], converters={0:str, 1:str})
df = df.astype({"binary": str})
df = df['binary'].str.split('', expand=True)
df.drop(columns=[0,13],inplace=True)

def oxygen_generator_rating(df):
    binary = ''
    # copy the dataframe
    df_copy = df.copy()
    # iterate through all the columns of df and find the most occuring bit for each col
    for col in df.columns:
        # find counts of all unique values in the column
        c = df_copy[col].value_counts()
        # print(c)
        if(col==12 or df_copy.shape[0]==1):
            val = df_copy[col]
            binary+=val
            break
        # find the most count of the value
        if(c[0] == c[1]):
            most = '1'
            binary+=most
        else:
            most = c.index[0]
            binary+=str(most)
        # print(col)
        # print(most)
        # print(type(most))
        # keep only the numbers starting with this digit
        for ind, row in df_copy.iterrows():
            # print("row is ", row)
            # print( row[col] )
            if(row[col]==most):
                continue
            else:
                df_copy.drop(ind, inplace=True)
    # print(binary)
    # print(df_copy)
    return int(binary.iloc[0],2)

oxygen_rating = oxygen_generator_rating(df)

def CO2_scrubber_rating(df):
    binary = ''
    # copy the dataframe
    df_copy = df.copy()
    # iterate through all the columns of df and find the most occuuing bit for each col
    for col in df.columns:
        # find counts of all unique values in the column
        c = df_copy[col].value_counts()
        # print(c)
        if(col==12 or df_copy.shape[0]==1):
            val = df_copy[col]
            binary+=val
            break
        # find the most count of the value
        if(c[0] == c[1]):
            most = '0'
            binary+=most
        else:
            most = c.index[1]
            binary+=str(most)
        # print(col)
        # print(most)
        # print(type(most))
        # keep only the numbers starting with this digit
        for ind, row in df_copy.iterrows():
            # print("row is ", row)
            # print( row[col] )
            if(row[col]==most):
                continue
            else:
                df_copy.drop(ind, inplace=True)
    #   print(df_copy)
    # print(df_copy)
    # print(binary)
    return int(binary.iloc[0],2)

CO2_rating = CO2_scrubber_rating(df)

life_support_rating = oxygen_rating * CO2_rating

print(life_support_rating)