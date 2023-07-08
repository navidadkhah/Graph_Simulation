import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import truncnorm

# Adjust distribution parameters to make mean and median approximately equal
mean = 100
std_dev = 30
lower_bound = 0
upper_bound = np.inf
median = mean

# Calculate distribution parameters for truncated normal distribution
a = (lower_bound - mean) / std_dev
b = (upper_bound - mean) / std_dev

# Generate random samples from the truncated normal distribution
samples = truncnorm.rvs(a, b, loc=mean, scale=std_dev, size=1000)

# Calculate scaled TTT values
scaled_ttt = -np.log(1 - (samples / samples.max()))

# Plot the scaled TTT transformations
plt.scatter(scaled_ttt, samples)
plt.xlabel('Scaled TTT')
plt.ylabel('Time')
plt.title('Scaled TTT Transformations for Node Lifetime Distributions')
plt.show()