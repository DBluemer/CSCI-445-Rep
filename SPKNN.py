import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn 

from sklearn import KNN
from sklearn.model_selection import train_test_split

raw_data = pd.read_csv('.csv')
print(raw_data)