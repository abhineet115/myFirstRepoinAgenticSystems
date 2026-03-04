import numpy as np

data = np.array([10, 20, 30, 40], dtype=float)

mean_val = np.mean(data)
std_val = np.std(data)

normalized_data = (data - mean_val) / std_val

reshaped_data = normalized_data.reshape(2, 2)

print(f"Original data: {data}")
print(f"Mean: {mean_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}")
print(f"Normalized data: {np.round(normalized_data, 2)}")
print(f"Reshaped data shape: {reshaped_data.shape}")