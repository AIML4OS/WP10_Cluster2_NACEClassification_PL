from typing import List, Tuple
import torch
import numpy as np
import pandas as pd
from typing import Tuple, List
from typing import List, Tuple


def embed_text(texts, tokenizer, model):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.cpu().numpy()

def read_csv_file(file_path: str) -> Tuple[List[str], List[str]]:
    df = pd.read_csv(file_path, sep=';')
    df_new = df
    df_new = df.loc[(df['symbol'].str.len() > 4) & (df['id'] >= 141) & (df['id'] <= 732) ][['symbol','nazwa','opisObejmujeNieobejmuje','id']]
    df_new['opis'] = df['nazwa'].fillna('')


    return df_new


df = read_csv_file('../Dane/clear_pkd.csv')
print(df)

# 3. Zapisujemy do CSV
df.to_csv("pkd.csv", index=False, encoding="utf-8", sep=';')   # lub "utf-8-sig" dla Excela po polsku


