COLLECTION_NAME = "pkd_database" # Name of collection
EMBEDDING_MODEL_NAME = "intfloat/multilingual-e5-large" ## Tested models intfloat/multilingual-e5-large || sdadas/polish-roberta-base-v2 || sdadas/mmlw-e5-base
RERANKER_MODEL_NAME = "BAAI/bge-reranker-v2-gemma" ##"BAAI/bge-reranker-v2-gemma"  Reranked LLM model for multilangual
RETRIEVER_K = 10 # How many records we return from retriever 
RERANKER_K = 3 # How many records return from reranked function

RAG_FILE = "../Dane/ALL_DATA_20.04.2026.csv" # ./source/pkd.csv | ../Dane/ALL_DATA_20.04.2026.csv 
CHROMA_PATH = "./database/chroma_pkd_pl_train_set"