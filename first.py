#Import statements
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')


#Import training data
train_df = pd.read_csv('train.csv')

#print(train_df.columns)

print(train_df['SalePrice'].describe())
