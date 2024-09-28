import json
import matplotlib.pyplot as plt
import pandas as pd

#Load the JSON data from the 'rawdata.json' file
with open(r'C:\Users\SANKEERTH\Downloads\rawdata.json', 'r') as file:
    data = json.load(file)

#Extract the 'vitals' from the data
vitals = data['vitals']  # Accessing the 'vitals' key directly

#Convert the vitals data into a pandas DataFrame
df = pd.DataFrame(vitals)

#Plotting
plt.figure(figsize=(12, 6))  # Increase figure size for better visibility
plt.plot(df['t'], df['e'], linestyle='-', linewidth=2, color='blue')  # Solid line, thicker width, red color
plt.title('Plot of e vs t (Timestamp in milliseconds)', fontsize=14)
plt.xlabel('Timestamp (ms)', fontsize=12)
plt.ylabel('e', fontsize=12)
plt.grid(True)  # Add a grid
plt.ylim(min(df['e']) - 10, max(df['e']) + 10)  # Set y-axis limits for better visualization
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Add horizontal line at y=0 for reference
plt.show()
