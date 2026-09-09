import numpy as np
import pandas as pd
import torch
from datasets import Dataset
from sklearn.metrics import top_k_accuracy_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, DataCollatorWithPadding


data = pd.read_csv('labels_encoder.csv',sep=',')
df_test = pd.read_csv('../Dane/test_set.csv')
df_test["text"] = df_test["opis"].astype(str)
test_dataset = Dataset.from_pandas(df_test[["text", "labels"]])

MODEL_PATH = "./final_model"
MAX_LEN = 128
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
trainer = Trainer(model=model,data_collator=DataCollatorWithPadding(tokenizer))
def tokenize(batch):
    return tokenizer(
        batch["text"],
        truncation=True,
        max_length=MAX_LEN,
        padding=False
    )
NUM_LABELS = len(data['labels'].unique())
test_dataset = test_dataset.map(
    tokenize,
    batched=True,
    remove_columns=["text"]
)
test_dataset.set_format(
    type="torch",
    columns=["input_ids", "attention_mask", "labels"]
)
### Top accurency 
# prediction output
pred_output = trainer.predict(test_dataset)
y_pred = np.argmax(pred_output.predictions, axis=-1)
y_true = pred_output.label_ids
probs = torch.softmax(
    torch.tensor(pred_output.predictions),
    dim=-1
).numpy()

top3 = top_k_accuracy_score(
    y_true,
    probs,
    k=3,
    labels=np.arange(NUM_LABELS)
)

top5 = top_k_accuracy_score(
    y_true,
    probs,
    k=5,
    labels=np.arange(NUM_LABELS)
)
top10 = top_k_accuracy_score(
    y_true,
    probs,
    k=10,
    labels=np.arange(NUM_LABELS)
)

print("Predykcja dla TOP3:", top3)
print("Predykcja dla TOP5:", top5)
print("Predykcja dla TOP10:", top10)
### Pojedyńcze predykcja

print("predykcja dla pojdedyńczego przypadku")
text = "projektowanie oraz budowa łodzi podwodnych"
print("predykcja dla: ",text)
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
y_pred = np.argmax(outputs.logits.detach().numpy(), axis=-1)
print(y_pred)
data = pd.read_csv('labels_encoder.csv',sep=',')
print(data.loc[data['labels']==y_pred[0]].head(1))

