import pandas as pd 
data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)

data=[["Raja",23],["Anbu",22],["Siva",25]]
df=pd.DataFrame(data,columns=["Name","Age"])
print(df)

df=pd.DataFrame(data,columns=["Name","Age"], dtype=float)
print(df)

#Dict of ndarrays
data={"Name":["Raja","Anbu","Siva"], "Age":[23,22,25]}
df=pd.DataFrame(data)
print(df)

#indexed DataFrame
data={"Name":["Raja","Anbu","Siva"], "Age":[23,22,25]}
df=pd.DataFrame(data, index=["I","II","III"])
print(df)

#List of Dictionaries
data=[{"Name":"Anbu","Age":22,"Mobile":7623873},
      {"Name":"Raja","Age":23,},
      {"Name":"Siva","Age":24,"Mobile":9878967}
      ]
df=pd.DataFrame(data)
print(df)

"""
NaN, standing for not a number, is a member of a numeric data type that can be interpreted as a value that is undefined or unrepresentable, 
especially in floating-point arithmetic.
"""

#List of Dictionaries
data=[{"Name":"Anbu","Age":22,"Mobile":7623873},
      {"Name":"Raja","Age":23,},
      {"Name":"Siva","Age":24,"Mobile":9878967}
      ]
df=pd.DataFrame(data, index=["Rank1","Rank2","Rank3"] , columns=["Name","Age","Mobile Number"] )
print(df)

























