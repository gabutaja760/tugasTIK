pca_script.py

import pandas as pd from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA import matplotlib.pyplot as plt

def run_pca(csv_path): data = pd.read_csv(csv_path) features =
data.columns x = data.values

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(x_scaled)

    pc_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
    print("Explained Variance Ratio:", pca.explained_variance_ratio_)

    plt.figure()
    plt.scatter(pc_df['PC1'], pc_df['PC2'])
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('PCA Scatter Plot')
    plt.savefig('pca_plot.png')
    plt.close()

if name == “main”: # Replace ‘data.csv’ with your file name
run_pca(‘data.csv’)
