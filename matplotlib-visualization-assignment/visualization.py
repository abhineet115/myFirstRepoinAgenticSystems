import matplotlib.pyplot as plt
import numpy as np

# List of 10 epochs
epochs = list(range(1, 11))

# Synthetic training loss: decaying exponential + small random noise
np.random.seed(42)
training_loss = np.exp(-np.array(epochs) * 0.3) + np.random.normal(0, 0.02, size=10)

print("Epochs:", epochs)
print("Training Loss:", training_loss)

plt.plot(epochs, training_loss,marker="o",color="b",linestyle="-",label="Tranning Loss")
plt.title("Training Loss vs Epochs")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

plt.scatter(epochs, training_loss,marker="o",label="Tranning Loss")
plt.title("Training Loss vs Epochs")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

models = ['Model A', 'Model C', 'Model B']
accuracies = [0.85, 0.88, 0.90]
plt.bar(models, accuracies, color=['skyblue', 'lightgreen', 'salmon'])
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Accuracy Comparison of Models')
plt.show()
