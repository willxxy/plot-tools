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


### PLOTTING TWO ONE D ARRAYS ON SAME PLOT 
N = 100  # Number of time points
gen_data = np.random.randn(N)  # Generating random data for demonstration
gt_data = np.random.randn(N)  # Generating random data for demonstration
time = np.arange(N)

# Creating a figure and a 1x2 subplot grid
fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # You can adjust the figure size

# First subplot
axs[0].plot(time, gen_data)
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Value')
axs[0].set_title('Generated Time Series Plot')

# Second subplot
axs[1].plot(time, gt_data)
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Value')
axs[1].set_title('Time Series Plot')

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('./side_by_side_plots.png')
