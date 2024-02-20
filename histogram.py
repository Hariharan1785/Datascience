import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(2000)
print(data)
plt.hist(data, color="red")
plt.title("Histogram of sample data")
plt.xlabel("Sample data")
plt.ylabel("Frequency of sample data")
plt.savefig("D:/histogram28jan24.png")
plt.show()

