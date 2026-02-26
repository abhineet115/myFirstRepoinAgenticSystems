import numpy as np

np.random.seed(0)

num_samples = 500
num_features =5
data = np.random.randn(num_samples, num_features)

mean = data.mean(axis=0)
std = data.std(axis=0)

normalized = (data - mean) / std
split_index = int(0.8 * num_samples)

train_data = normalized[:split_index]
test_data = normalized[split_index:]

print("Original data shape:", data.shape)
print("Mean shape:", mean.shape)
print("standard deviation:",std.shape)
print("Training data shape:", train_data.shape)
print("Test data shape:", test_data.shape)
print("Note: Modifying the slice affected the original array")
