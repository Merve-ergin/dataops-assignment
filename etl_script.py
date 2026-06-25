import pandas as pd
from sqlalchemy import create_engine

def run_etl():
    print("--- ETL Süreci Başladı ---")
    
    url = "https://raw.githubusercontent.com/erkansirin78/datasets/refs/heads/master/dirty_store_transactions.csv"
    print("Veri kaynağından indiriliyor...")
    df = pd.read_csv(url)
    
    print("Veri temizleniyor...")
    df.columns = df.columns.str.strip().str.lower()
    df.drop_duplicates(inplace=True)
    
    if 'transaction_id' in df.columns:
        df.dropna(subset=['transaction_id'], inplace=True)
    
    if 'transaction_date' in df.columns:
        df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
    
    print("PostgreSQL 'traindb' veritabanına yazılıyor...")
    
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/traindb')
    
    df.to_sql(
        name='clean_data_transactions', 
        con=engine, 
        schema='public', 
        if_exists='replace', 
        index=False
    )
    print("--- ETL Süreci Başarıyla Tamamlandı! ---")

if __name__ == "__main__":
    run_etl()