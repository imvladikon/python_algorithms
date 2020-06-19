import numpy as np

def k_means(data, k, centroids, max_iter=100):
    """
    Perform clustering using K-means algorithm
    :param data: observations
    :param k: number of clusters to cluster into
    :param centers: initial cluster centers
    :return: tuple of:
       1. Final cluster centers
       2. Assignments - np.array with cluster numer each observation is assigned to
       3. WCSS calculation

    """
    n_samples, n_features = data.shape
    labels = np.random.randint(low=0, high=k, size=n_samples)
    n_ter = 0
    while n_ter < max_iter:
        n_ter += 1
        labels = (np.sqrt((np.square(data[:, np.newaxis] - centroids).sum(axis=2)))).argmin(axis=1)
        new_centers = np.array([data[labels == i].mean(0) for i in range(k)])
        if np.allclose(centroids, new_centers):
            break
        centroids = new_centers
    wcss = np.sum(np.sqrt((np.square(data[:, np.newaxis] - centroids).sum(axis=2))))
    return centroids, labels, wcss