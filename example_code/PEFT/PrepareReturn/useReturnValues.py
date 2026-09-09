import numpy as np
import torch
from datasets import Dataset
from sklearn.metrics import top_k_accuracy_score
from PrepareModel.useModel import trainer


def return_trainer_pred(test_dataset):
    return trainer.predict(test_dataset)

def return_pred(test_dataset):
    pred_output = return_trainer_pred(test_dataset)
    y_pred = np.argmax(pred_output.predictions, axis=-1)
    y_true = pred_output.label_ids

    return y_pred, y_true,pred_output

def return_top_results(test_dataset, NUM_LABELS):
    y_pred, y_true, pred_output = return_pred(test_dataset)

    pred_output = pred_output

    probs = torch.softmax(torch.tensor(pred_output.predictions),dim=-1).numpy()

    top3 = top_k_accuracy_score( y_true,probs,k=3,labels=np.arange(NUM_LABELS))
    top5 = top_k_accuracy_score(y_true,probs,k=5,labels=np.arange(NUM_LABELS))
    top10 = top_k_accuracy_score(y_true,probs,k=10,labels=np.arange(NUM_LABELS))
    return top3,top5,top10