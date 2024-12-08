#Data Preprocessing and Feature Extraction

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load the CSV file into a DataFrame
capture_df = pd.read_csv('C:/Users/smedishetty1/OneDrive/Documents/Cyber_Projects/NIDS/capture.csv')

# Display basic information about the dataset
print(capture_df.info())

# Display first few rows of the dataset
print(capture_df.head())

# Handle missing values (if any)
capture_df.fillna(method='ffill', inplace=True)

# Normalize numerical features
scaler = MinMaxScaler()
capture_df[['time', 'length']] = scaler.fit_transform(capture_df[['time', 'length']])

# Encode categorical features
label_encoder = LabelEncoder()
capture_df['proto'] = label_encoder.fit_transform(capture_df['proto'])

# Save the cleaned and normalized data
capture_df.to_csv('C:/Users/smedishetty1/OneDrive/Documents/Cyber Projects/NIDS/capture_processed.csv', index=False)

print(capture_df.head())
