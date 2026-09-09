import pandas as pd
from datasets import Dataset
from PrepareModel.useModel import trainer,tokenize

def prepare_test_set(test_set_path: str):
    df_test = pd.read_csv(test_set_path)
    df_test["text"] = df_test["opis"].astype(str)
    test_dataset = Dataset.from_pandas(df_test[["text", "labels"]])

    test_dataset = test_dataset.map(
        tokenize,
        batched=True,
        remove_columns=["text"]
    )
    test_dataset.set_format(
        type="torch",
        columns=["input_ids", "attention_mask", "labels"]
    )
    return test_dataset