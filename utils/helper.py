import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from sklearn.metrics import confusion_matrix
from sklearn.base import BaseEstimator, TransformerMixin

def predict_and_plot(model, inputs, targets, name=''):
    preds = model.predict(inputs)
    cf = confusion_matrix(targets, preds, normalize='true')
    plt.figure()
    sns.heatmap(cf, annot=True)
    plt.xlabel('Prediction')
    plt.ylabel('Target')
    plt.title('{} Confusion Matrix'.format(name))
    
    return preds

class EducationProcess(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        data = np.where(data.isin([1, 2, 3]), 1, data)
        data = pd.Series(data.flatten()).replace({4: 2, 5: 3, 6: 4})
        return pd.DataFrame(data, columns=X.columns)