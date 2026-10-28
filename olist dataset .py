import pandas as pd
import numpy as np
df= pd.read_csv(r"olist_customers_dataset.csv")
df.head()
print(df.shape)
print(df.columns)
print(df.describe())
print(df.isnull().sum())
print(df.info())
print(df.duplicated())
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate customer_id:",
      df["customer_id"].duplicated().sum())

print("Duplicate customer_unique_id:",
      df["customer_unique_id"].duplicated().sum())

df1=pd.read_csv(r"olist_geolocation_dataset.csv")
df.head()
print(df1)
print(df1.shape)
print(df1.columns)
print(df1.describe())
print(df1.isnull().sum())
print(df1.info())
print("duplicate city:",
    df1["geolocation_city"].duplicated().sum())
print("duplicate state:",
    df1["geolocation_state"].duplicated().sum())

duplicate_counts = df1.apply(lambda col: col.duplicated().sum())

print(duplicate_counts)
 
 
df2=pd.read_csv(r"olist_order_items_dataset.csv")
df2.head()
print(df2)
print(df2.shape)
print(df2.columns)
print(df2.describe())
print(df2.isnull().sum())
print(df2.info())

duplicate_counts = df2.apply(lambda col: col.duplicated().sum())

print(duplicate_counts)
 
 
df3= pd.read_csv(r"olist_order_payments_dataset.csv")
df3.head()
print(df3)
print(df3.shape)
print(df3.columns)
print(df3.describe())
print(df3.isnull().sum())
print(df3.info())

duplicate_counts = df3.apply(lambda col: col.duplicated().sum())

print(duplicate_counts)


df4= pd.read_csv(r"olist_order_reviews_dataset.csv")
df4.head()
print(df4)
print(df4.shape)
print(df4.columns)
print(df4.describe())
print(df4.isnull().sum())
print(df4[['review_comment_message','review_comment_title']])
df4['review_comment_message']= df4['review_comment_message'].fillna('no review')
df4['review_comment_title']= df4['review_comment_title'].fillna('no review')
print(df4.isnull().sum())

print(df4.info())

duplicate_counts = df4.apply(lambda col: col.duplicated().sum())

print(duplicate_counts)


df5= pd.read_csv(r"Olist_orders_dataset.csv")
df5.head()
print(df5)
print(df5)
print(df5.shape)
print(df5.columns)
print(df5.describe())
print(df5.isnull().sum())
df5['order_approved_at']=pd.to_datetime(df5['order_approved_at'])
df5['order_approved_at']=df5['order_approved_at'].interpolate()
df5['order_delivered_carrier_date']=pd.to_datetime(df5['order_delivered_carrier_date'])
df5['order_delivered_carrier_date']=df5['order_delivered_carrier_date'].interpolate()
df5['order_delivered_customer_date']=pd.to_datetime(df5['order_delivered_customer_date'])
df5['order_delivered_customer_date']=df5['order_delivered_customer_date'].interpolate()
print(df5.isnull().sum())
print(df5.info())

duplicate_counts = df5.apply(lambda col: col.duplicated().sum())

print(duplicate_counts)


df6=pd.read_csv(r"olist_products_dataset.csv")
df6.head()
print(df6)
print(df6)
print(df6.shape)
print(df6.columns)
print(df6.describe())
print(df6.isnull().sum())

med_category = df6['product_category_name']=df6['product_category_name'].fillna(df6['product_category_name'].mode()[0])
print(med_category)
df6['product_name_lenght']=df6['product_name_lenght'].fillna(df6['product_name_lenght'].median())
df6['product_description_lenght']=df6['product_description_lenght'].fillna(df6['product_description_lenght'].median())
df6['product_photos_qty']=df6['product_photos_qty'].fillna(df6['product_photos_qty'].median())
df6['product_weight_g']=df6['product_weight_g'].fillna(df6['product_weight_g'].median())
df6['product_length_cm']=df6['product_length_cm'].fillna(df6['product_length_cm'].median())
df6['product_height_cm']=df6['product_height_cm'].fillna(df6['product_height_cm'].median())
df6['product_width_cm']=df6['product_width_cm'].fillna(df6['product_width_cm'].median())
print(df6.isnull().sum())
print(df6.info())

duplicate_counts = df6.apply(lambda col: col.duplicated().sum())

print(duplicate_counts)



df7=pd.read_csv(r"olist_sellers_dataset.csv")
df7.head()
print(df7)
print(df7)
print(df7.shape)
print(df7.columns)
print(df7.describe())
print(df7.isnull().sum())
print(df7.info())

duplicate_counts = df7.apply(lambda col: col.duplicated().sum())

print(duplicate_counts)


df8= pd.read_csv(r"product_category_name_translation.csv")
df8.head()
print(df8)
print(df8)
print(df8.shape)
print(df8.columns)
print(df8.describe())
print(df8.isnull().sum())
print(df8.info())

duplicate_counts = df8.apply(lambda col: col.duplicated().sum())

print(duplicate_counts)

## export files to sql

import sqlalchemy
from sqlalchemy import create_engine
from pathlib import Path

username = "postgres"
host = "localhost"
port = "5432"
password = "DB_PASSWORD"
database = "olist_project"
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")


# Store all 9 DataFrames with their table names
dataframes = {
    "olist_customers": df,
    "olist_geolocation": df1,
    "olist_order_items": df2,
    "olist_order_payments": df3,
    "olist_order_reviews": df4,
    "olist_orders": df5,
    "olist_products": df6,
    "olist_sellers": df7,
    "olist_product_category": df8
}

# Transfer all DataFrames to PostgreSQL
for table_name, dataframe in dataframes.items():
    dataframe.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )
    print(f"{table_name} transferred successfully!")

engine.dispose()
