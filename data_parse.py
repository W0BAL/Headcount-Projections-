import pandas as pd
import numpy as np

df = pd.read_excel('headcount.xlsx')


results = []

# Iterate through the DataFrame
for index, row in df.iterrows():
    
    # Check if the cell in the first column is a number (which will be the day)
    if isinstance(row.iloc[0], (int, float)) and not np.isnan(row.iloc[0]):
        day = int(row.iloc[0])
        hours = df.iloc[index + 1, 2:].values
        
        # Extract sections and their respective headcounts
        for offset in range(1, 6):  # We expect 5 sections based on your data description
            section_row = index + offset
            
            # Check if we exceed the number of rows in the DataFrame
            if section_row >= len(       df):
                break
            
            section = df.iloc[section_row, 1]
            headcounts = df.iloc[section_row, 2:2+len(hours)].values
            
            for h, hc in zip(hours, headcounts):
                try:
                    hc_float = float(hc)
                    if not np.isnan(hc_float):  # Filter out NaN headcounts
                        results.append([day, h, section, hc_float])
                except ValueError:
                    continue

# Convert the list to a DataFrame
final_df = pd.DataFrame(results, columns=['Day', 'Hour', 'Section', 'Headcount'])

day_summary = final_df.groupby(['Day', 'Section'])['Headcount'].sum().reset_index()
print(day_summary)

