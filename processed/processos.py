import pandas as pd 
import os

os.makedirs("data_lake/raw", exist_ok= True)
os.makedirs("data_lake/processed", exist_ok= True)
os.makedirs("data_lake/curated", exist_ok= True)

#raw

df_raw= pd.DataFrame([

    {"cliente": "Ana", "valor": 200, "data": "2025-08-21"},

    {"cliente": "João", "valor": None, "data": "2025-08-21"},

    {"cliente": "Maria", "valor": 350, "data": "2025-08-21"},

    {"cliente": "Pedro", "valor": 400, "data": "2025-08-21"},

    {"cliente": "Ana", "valor": 150, "data": "2025-08-22"},

    {"cliente": "João", "valor": 300, "data": "2025-08-22"},

    {"cliente": "Maria", "valor": None, "data": "2025-08-22"},

    {"cliente": "Pedro", "valor": 500, "data": "2025-08-22"},

    {"cliente": "Ana", "valor": 250, "data": "2025-08-23"}, 

    {"cliente": "João", "valor": 400, "data": "2025-08-23"},

    {"cliente": "Maria", "valor": 450, "data": "2025-08-23"},

])

df_raw.to_json("data_lake/raw/vendas.json", orient="records", lines=True)

#processed

df_processed= df_raw.dropna(subset=["valor"])
df_processed.loc[:, "data"]= pd.to_datetime(df_processed["data"])
df_processed.to_parquet("data_lake/processed/vendas.parquet")

#curated

df_curated= df_processed.groupby("cliente")["valor"].sum().reset_index()
df_curated.to_parquet("data_lake/curated/vendas_final.parquet")

print("Data Lake criado com : RAW -- PROCESSED -- CURATED ")
