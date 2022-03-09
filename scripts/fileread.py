import numpy as np
import pandas as pd

managers_data = pd.read_csv("./mock/fake_managers.csv", delimiter=",")
properties_data = pd.read_csv("./mock/fake_properties.csv", delimiter=",")
residents_data = pd.read_csv("./mock/fake_residents.csv", delimiter=",")

# Replacing NA values with null
managers_data = managers_data.replace(np.nan, None)
properties_data = properties_data.replace(np.nan, None)
residents_data = residents_data.replace(np.nan, None)

# Converting each row into a tuple
managers_tuples = [tuple(row) for row in managers_data.values]
properties_tuples = [tuple(row) for row in properties_data.values]
residents_tuples = [tuple(row) for row in residents_data.values]
