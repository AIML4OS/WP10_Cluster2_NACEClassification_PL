import pandas as pd
import numpy as np
from PrepareModel.useModel import trainer,tokenize,tokenizer,model
from PrepareTestset.useTestset import prepare_test_set
from PrepareReturn.useReturnValues import return_top_results


label_encoder = pd.read_csv('labels_encoder.csv',sep=',')
NUM_LABELS = len(label_encoder['labels'].unique())

test_dataset = prepare_test_set('test_set.csv')

top3, top5, top10 = return_top_results(test_dataset, NUM_LABELS)

print(f"Top results: 3: {top3} , 5: {top5}, 10: {top10}")
print('#################')
print("Predict for text: ")
text = "Przetwarzanie i konserwowanie mięsa, z wyłączeniem mięsa z drobiu"

inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
y_pred = np.argmax(outputs.logits.detach().numpy(), axis=-1)

label_encoder.loc[label_encoder['labels']==y_pred[0]].head(1)
print(label_encoder.loc[label_encoder['labels']==y_pred[0]].head(1))