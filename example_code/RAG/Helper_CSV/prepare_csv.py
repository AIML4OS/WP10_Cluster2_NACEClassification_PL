import numpy as np
import pandas as pd
import os
from typing import Tuple, List
from typing import List, Tuple

def prepare_pkd_data(csv_path: str) ->pd.DataFrame:
    if file_exists(csv_path) == 0:
        return None
    else:
        df = pd.read_csv(csv_path, sep=';', encoding='utf-8')
        df = df[['PKD_2007','description_PL']]
        df = df.rename(columns={
            'PKD_2007': 'kod_pkd', 
            'description_PL': 'opis'
        })
        df['kod_pkd'] = df['kod_pkd'].astype(str).str.strip()
        df['opis'] = (
            df['opis']
                .str.lower()
                .str.strip()
                .str.replace(r"\s+", " ", regex=True)
            )
        df = df[df['opis'].str.len() > 20]
        df = df[['kod_pkd', 'opis']].dropna()
        df = df.drop_duplicates()

        print(f"Wszystkie dane: {len(df)} rekordów (do RAG)")
        return df

def file_exists(csv_path: str) -> bool:
    if not os.path.exists(csv_path):
        return 0
    else:
        return 1