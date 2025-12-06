# import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score


# load data original copies
z_customer = pd.read_csv("C:\\Users\\young\\OneDrive\\Documents\\Masters\\Fall 2025\\IS6813 Capstone 3\\data\\customer.csv")
z_cutoff_time = pd.read_csv("C:\\Users\\young\\OneDrive\\Documents\\Masters\\Fall 2025\\IS6813 Capstone 3\\data\\cutoff_times.csv.csv")
z_google_a = pd.read_csv("C:/Users/young/OneDrive/Documents/Masters/Fall 2025/IS6813 Capstone 3/data/google_analytics.csv")
z_material = pd.read_csv("C:/Users/young/OneDrive/Documents/Masters/Fall 2025/IS6813 Capstone 3/data/material.csv")
z_op_hours = pd.read_csv("C:/Users/young/OneDrive/Documents/Masters/Fall 2025/IS6813 Capstone 3/data/operating_hours.csv")
z_orders = pd.read_csv("C:/Users/young/OneDrive/Documents/Masters/Fall 2025/IS6813 Capstone 3/data/orders.csv")
z_sales = pd.read_csv("C:/Users/young/OneDrive/Documents/Masters/Fall 2025/IS6813 Capstone 3/data/sales.csv")
z_visit_plan = pd.read_csv("C:/Users/young/OneDrive/Documents/Masters/Fall 2025/IS6813 Capstone 3/data/visit_plan.csv")