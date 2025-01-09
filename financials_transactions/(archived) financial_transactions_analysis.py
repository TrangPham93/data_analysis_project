#%%
import pandas as pd
import numpy as np

# %% #user this to run part of the code

# 1. Load the data
# %%
cards_df = pd.read_csv("cards_data.csv")
cards_df = cards_df.set_index("id").sort_index()
print(cards_df.head())


# %%
transaction_df = pd.read_csv("transactions_data.csv")
# transaction_df = transaction_df.set_index("id").sort_index()
print(transaction_df.head())


# %%
cards_transaction_df = pd.read_csv("cards_data.csv")
cards_transaction_df = cards_transaction_df.set_index("id").sort_index()
print(cards_transaction_df.head())

# 2. Data Inspection
#%%
# 3. Data Cleaning


# 4. Data Exploration

