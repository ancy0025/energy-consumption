# Energy Consumption Analysis using YAFS

## Overview
This project analyzes energy consumption using the **Yet Another Fog Simulator (YAFS)** framework. It simulates and evaluates energy efficiency in distributed computing environments such as fog and edge computing.

## Features
- **Energy Consumption Analysis:** Simulates and records energy usage in distributed systems.
- **Customizable Parameters:** Modify configurations for different simulation scenarios.
- **Results Visualization:** Generates energy consumption reports and insights.
- **Streamlit Deployment:** Interactive web-based dashboard to visualize results.

## Installation
To set up and run the project, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Install Dependencies
Make sure you have Python 3.9 or higher installed. Then, run:
```bash
pip install -r requirements.txt
```

### 3. Run the Simulation
```bash
python main.py
```
This will generate the output file `results/energy_consumption.csv`.

## Usage
After running the simulation, analyze the energy consumption data stored in `results/energy_consumption.csv`. You can visualize the data using Python or upload it to the Streamlit app for better insights.

## Deploying on Streamlit
You can visualize the results using Streamlit. To do this:

### 1. Install Streamlit
```bash
pip install streamlit
```

### 2. Run the Streamlit App
```bash
streamlit run app.py
```

### 3. Deploy on Streamlit Cloud
To deploy the app online using Streamlit Cloud:
- Push your code to GitHub.
- Go to [Streamlit Cloud](https://share.streamlit.io/).
- Connect your GitHub repository and deploy the `app.py` file.

## File Structure
```
📂 your-repo/
├── 📁 results/                  # Output results
│   ├── energy_consumption.csv   # Energy consumption data
├── main.py                      # Simulation script
├── app.py                       # Streamlit dashboard
├── requirements.txt              # Dependencies
├── README.md                     # Project documentation
```

## License
This project is licensed under the **Apache 2.0 License**. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact
For any questions or support, reach out via email or GitHub issues.

---
**Happy Coding! 🚀**

