
import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2000, 2005, 2010, 2015, 2020, 2024]
publications = [28, 46, 82, 142, 182, 189]
peak_2023 = [2023, 204]

# Regression line (y = 8.1x + 24.7, x = Year - 2000)
x_reg = np.array([year - 2000 for year in years])
y_reg = 8.1 * x_reg + 24.7

# Create plot
plt.figure(figsize=(8, 6))  # 4:3 aspect ratio for journal
plt.plot(years, publications, marker='o', color='blue', linewidth=2, markersize=8, label='Publications')
plt.plot(years, y_reg, linestyle='--', color='gray', linewidth=1.5, label='Regression (R²=0.91)')
plt.scatter(peak_2023[0], peak_2023[1], color='red', s=100, label='2023 Peak')

# Annotations
plt.annotate('Peak (204)', (2023, 204), xytext=(2023, 210), fontsize=10, fontfamily='Arial',
             ha='center', va='bottom')
plt.annotate('Post-2010 Acceleration', (2010, 82), xytext=(2010, 100), fontsize=10, fontfamily='Arial',
             ha='center', va='bottom')

# Title and axes labels
plt.title('Trends in MCDM Publications, 2000–2024', fontsize=14, fontfamily='Arial', pad=10)
plt.xlabel('Year', fontsize=12, fontfamily='Arial')
plt.ylabel('Number of Publications', fontsize=12, fontfamily='Arial')

# Grid and ticks
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(years, fontsize=10, fontfamily='Arial')
plt.yticks(np.arange(0, 251, 50), fontsize=10, fontfamily='Arial')

# Legend
plt.legend(fontsize=10, loc='upper left')

# Save outputs
plt.savefig('Trends_in_Topics_2000_2024.png', dpi=300, bbox_inches='tight')
plt.savefig('Trends_in_Topics_2000_2024.svg', format='svg', bbox_inches='tight')
plt.close()