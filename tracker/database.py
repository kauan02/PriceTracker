import pandas as pd
from sqlalchemy import create_engine
from scraper import GetInfo

def AddDB():
    datetime, product_name, normal_price, price = GetInfo()
    print(datetime, product_name, normal_price, price)
    engine = create_engine('postgresql://postgres:senha1234@localhost:5432/prices')
    df = pd.DataFrame({
        "date": [datetime],
        "name": [product_name],
        "original price": [normal_price],
        "sale price": [price]
    })
    
    df.to_sql('prices', engine, if_exists='append', index=False)
    
def ShowDB():
    engine = create_engine('postgresql://postgres:senha1234@localhost:5432/prices')
    df = pd.read_sql('prices', engine)
    print(df)
    
if __name__ == "__main__":
    AddDB()
    ShowDB()