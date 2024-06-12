import pandas as pd 
import numpy as np

Data = pd.read_csv('cicids2017.csv')
print(Data.info())

# Shuffle the dataset
Data = Data.sample(frac=1, random_state=42).reset_index(drop=True)

# Calculate the number of rows in each partition
partition_size = len(Data) // 6   # ps = 10   when data size is 60

# Create empty lists to store the partitions
partitions = []

# Split the dataset into 5 partitions
for i in range(6):
    start_index = i * partition_size  # = 0*10  = 0
    end_index = (i + 1) * partition_size  # 
    partition = Data.iloc[start_index:end_index]
    partitions.append(partition)
    
    # Save each partition to a CSV file
    partition.to_csv(f'partition_{i+1}.csv', index=False)
