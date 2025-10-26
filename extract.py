import pandas as pd

print( "Extract Data")

data={

    "id":[101,102,103],
    "name":["Ajay","komal","priti"],
    "age":[25,24,26]
}

df=pd.DataFrame(data)
print(df)