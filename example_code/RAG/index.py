import pandas as pd
import time
import datetime
from Helper_CSV.prepare_csv import prepare_pkd_data
from DataBase.rag_database import build_rag_database,retrieve_context
from conf import CHROMA_PATH,RAG_FILE
from sklearn.model_selection import train_test_split

start_perf = time.perf_counter()
start_timestamp = datetime.datetime.now()

def return_RAG_predict(text):
    query = str(text)
    context = retrieve_context(query, rag_collection, top_k=3)
    return context
    
if __name__ == "__main__":
    print(f"Start APP: {start_timestamp.strftime('%H:%M:%S.%f')[:-3]}")
    data = prepare_pkd_data(RAG_FILE)
    if data is not None:
        df_train, df_test = train_test_split(data, test_size=0.2, stratify=data["kod_pkd"])
        rag_collection = build_rag_database(df_train, CHROMA_PATH)
        print("Read data collection")
        print("New data prepare ... ")
        sample_df = df_test.sample(100).copy()
        sample_df['predict_PKD'] = sample_df['opis'].apply(return_RAG_predict)
        sample_df = sample_df.reset_index(drop=True)
        sample_df.to_csv("./Output/predict_PKD_100_ALL_DATA_RAG.csv", sep="#")
        print("End process")
    else:
        print("!! Problem with vectorise database !! ")

    end_perf = time.perf_counter()
    end_timestamp = datetime.datetime.now()

    total_work_time = end_perf - start_perf

print(f"End appliacation: {end_timestamp.strftime('%H:%M:%S.%f')[:-3]}")
print(f"Total time: {total_work_time / 60:.4f} miute")