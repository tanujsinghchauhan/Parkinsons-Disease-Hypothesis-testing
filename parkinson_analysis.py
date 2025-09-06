import pandas as pd

# Load dataset from local file after downloading
df = pd.read_csv('parkinsons.data')

# View first rows to understand structure
print(df.head())

# Partition data into groups based on 'status' column
# 'status' == 1 means PD patient, 'status' == 0 means healthy control
pd_group = df[df['status'] == 1]
control_group = df[df['status'] == 0]

# Print size of each group
print("Number of PD samples:", pd_group.shape[0])
print("Number of control samples:", control_group.shape[0])

from scipy.stats import ttest_ind

# List of selected features based on clinical relevance
features = ['MDVP:Fo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Shimmer', 'HNR']

# Dictionary to store results
results = {}

for feature in features:
    pd_values = pd_group[feature]
    control_values = control_group[feature]
    t_stat, p_val = ttest_ind(pd_values, control_values)
    results[feature] = {'t-statistic': t_stat, 'p-value': p_val}

# Print results
for feature, metrics in results.items():
    print(f"{feature} - t-statistic: {metrics['t-statistic']:.4f}, p-value: {metrics['p-value']:.4f}")

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x='status', y='MDVP:Fo(Hz)', data=df)
plt.xticks([0, 1], ['Control', 'PD'])
plt.title('Distribution of MDVP:Fo(Hz) by Group')
plt.show()