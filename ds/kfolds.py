class KFolds:
    def __init__(self, n_splits):
        self.n_splits = n_splits

    def get_n_splits(self):
        return self.n_splits

    def split(self, X):
        indices = np.arange(X.shape[0])
        for test_index in self._iter_test_masks(X):
            train_index = indices[np.logical_not(test_index)]
            test_index = indices[test_index]
            yield train_index, test_index
    def _iter_test_masks(self, X):
        for test_index in self._iter_test_indices(X):
            test_mask = np.zeros(X.shape[0], dtype=np.bool)
            test_mask[test_index] = True
            yield test_mask
    def _iter_test_indices(self, X):
        n_samples = X.shape[0]
        indices = np.arange(n_samples)
        n_splits = self.n_splits
        fold_sizes = np.full(n_splits, n_samples // n_splits, dtype=np.int)
        fold_sizes[:n_samples % n_splits] += 1
        current = 0
        for fold_size in fold_sizes:
            start, stop = current, current + fold_size
            yield indices[start:stop]
            current = stop