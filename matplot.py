import matplotlib.pyplot as plt
import numpy as np

### PLOTTING ONE D ARRAY
# Sample data (replace this with your actual data array)
N = 100  # Number of time points
data = np.random.randn(N)  # Generating random data for demonstration

# Time axis (assuming equal intervals and starting from 0)
time = np.arange(N)

# Plotting the time series
plt.plot(time, data)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Time Series Plot')
plt.show()
