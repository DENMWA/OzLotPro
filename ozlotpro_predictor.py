
import numpy as np
import pandas as pd

def generate_predictions(n_sets=200):
    predictions = []
    for _ in range(n_sets):
        prediction = sorted(np.random.choice(range(1, 46), 7, replace=False))
        predictions.append(prediction)
    return pd.DataFrame(predictions, columns=[f"N{i+1}" for i in range(7)])
