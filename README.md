# Energy Consumption Analysis in YAFS

## Overview
This repository provides an energy consumption analysis using the **YAFS** (Yet Another Fog Simulator) framework. The simulation results are stored in `results/energy_consumption.csv`, capturing power usage across different components in a fog computing environment.

## Installation
To use this repository, ensure you have Python 3.9+ and install the required dependencies:

```sh
pip install -r requirements.txt
```

Alternatively, install YAFS directly from GitHub:

```sh
pip install git+https://github.com/acsicuib/YAFS@YAFS3#egg=yafs
```

## Running the Simulation
Execute the following command to start the simulation:

```sh
python main.py
```

This will generate energy consumption data, which is saved in:

```
results/energy_consumption.csv
```

## Energy Consumption Analysis
The `energy_consumption.csv` file contains structured data for analyzing power usage in the fog environment. The typical structure includes:

| Timestamp | Node ID | Energy Consumed (Joules) |
|-----------|--------|------------------|
| 0.1       | 1      | 0.5              |
| 0.2       | 2      | 0.7              |
| 0.3       | 3      | 1.2              |

### Visualizing Energy Data
To plot the energy consumption trends, use:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results/energy_consumption.csv')
plt.plot(df['Timestamp'], df['Energy Consumed (Joules)'])
plt.xlabel('Time (s)')
plt.ylabel('Energy (Joules)')
plt.title('Energy Consumption Over Time')
plt.show()
```

## Contributing
Feel free to submit issues and pull requests to improve the energy consumption analysis in YAFS.

## License
This project is licensed under the MIT License.

