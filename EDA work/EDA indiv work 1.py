# Individual work for the EDA for the Capstone 3 class, Fall 2025

import pandas as pd

#loading data
o_material = pd.read_csv("C:\\Users\\young\\OneDrive\\Documents\\Masters\\Fall 2025\\IS6813 Capstone 3\\data\\material.csv")

#create copy
material = o_material.copy()

#Basic overview of material
print(material.info())     # Data Types and non-null counts
# material.describe()  # confirmation of data types and non-null counts, duplicate, commented out

#search for NA
print(material.isna().sum())

## Data load for Google Analytics
o_google = pd.read_csv("C:\\Users\\young\\OneDrive\\Documents\\Masters\\Fall 2025\\IS6813 Capstone 3\\data\\google_analytics.csv")

#create copy
google_a = o_google.copy()

#review google_a data
print(google_a.info())


## Data load for Orders
o_orders = pd.read_csv("C:\\Users\\young\\OneDrive\\Documents\\Masters\\Fall 2025\\IS6813 Capstone 3\\data\\orders.csv")

#create copy
orders = o_orders.copy()

## Data load for Sales
o_sales = pd.read_csv("C:\\Users\\young\\OneDrive\\Documents\\Masters\\Fall 2025\\IS6813 Capstone 3\\data\\sales.csv")

#create copy
sales = o_sales.copy()
