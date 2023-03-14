import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans


# load the csv file into a pandas dataframe
df = pd.read_csv("train.csv")

# print the first few rows of the dataframe
print(df.head())

# Calculate descriptive statistics
print(df.describe())

# Create a histogram of the tBodyAcc-mean()-X column
plt.hist(df['tBodyAcc-mean()-X'], bins=50)
plt.title('tBodyAcc-mean()-X')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Create scatter plot for tBodyAcc-mean()-X and tBodyAcc-mean()-Y
plt.scatter(df['tBodyAcc-mean()-X'], df['tBodyAcc-mean()-Y'])

# Set axis labels and plot title
plt.xlabel('tBodyAcc-mean()-X')
plt.ylabel('tBodyAcc-mean()-Y')
plt.title('Scatter plot for tBodyAcc-mean()-X and tBodyAcc-mean()-Y')

# Show plot
plt.show()


# Create a box plot for each feature
#for feature in df.columns[:-1]:
 #   sns.boxplot(x='Activity', y=feature, data=df)
    
    
# Preprocess data
X = df.values

# Choose number of clusters
k = 3

# Apply k-means algorithm
kmeans = KMeans(n_clusters=k, random_state=0).fit(X[:, :-1])

# Get cluster labels
labels = kmeans.labels_

# Get cluster centers
centers = kmeans.cluster_centers_

# Visualize results
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()


# Create a correlation matrix
corr_matrix = df.corr()

# Select the features with correlation higher than a threshold value
threshold = 0.5
corr_features = set()
for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > threshold:
            colname = corr_matrix.columns[i]
            corr_features.add(colname)

# Print the selected features
print(corr_features)
