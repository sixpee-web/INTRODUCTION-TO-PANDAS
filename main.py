import pandas as pd
import numpy as np

exam_data = {
    'names': ['George vivien', 'Elizabeth','Avery', 'Chukwumobi', 'Amanda', 'Jenessa', 'Rhema'],
    'score': [12.3, np.nan, 13.8, 10.9, 19, np.nan, 17.4],
    'pass': ['yes','no', 'yes', 'no', 'yes', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
df = pd.DataFrame(exam_data , index=labels)

print("summary of class performance in test data, as a data frame")
print(df.info())