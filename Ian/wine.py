import psycopg2
import sqlalchemy
from sqlalchemy import create_engine


# importing pandas module 
import pandas as pd 

connection_string = f"postgres://pyuepqwjtgkmfx:75425df2df071f0b81f4e7bca3ad4f7e5cbefb361b0c30331d30196e3b8ef83a@ec2-34-198-31-223.compute-1.amazonaws.com:5432/da75s215ag1n2i"
engine = create_engine(f'postgres://pyuepqwjtgkmfx:75425df2df071f0b81f4e7bca3ad4f7e5cbefb361b0c30331d30196e3b8ef83a@ec2-34-198-31-223.compute-1.amazonaws.com:5432/da75s215ag1n2i')

# making data frame from csv file 
redwine = pd.read_csv("/Users/jeffhitt/Desktop/JeffGitHW/RedWine/winequality-red.csv")

# import df to sql
redwine.to_sql(name='redwine', con=engine, if_exists='append', index=False)

# making data frame from csv file 
whitewine = pd.read_csv("/Users/jeffhitt/Desktop/JeffGitHW/RedWine/winequality-white.csv")

# import df to sql
whitewine.to_sql(name='whitewine', con=engine, if_exists='append', index=False)