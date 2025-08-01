# Bibliometric-Visualization-For-Publication

## Overview

This project provides visualizations for bibliometric analysis, focusing on trends in publications and conceptual structure mapping using Multiple Correspondence Analysis (MCA). The visualizations are generated using Python scripts and are saved in both PNG and SVG formats for high-quality publication use.

---

## Features

- **Trends in Publications (2000–2024):**

  - Visualizes the number of publications per year.
  - Includes a regression line and highlights key trends and peaks.
  - Output: `Trends_in_Topics_2000_2024.png` and `Trends_in_Topics_2000_2024.svg`.

- **MCA Conceptual Structure Map:**
  - Plots keywords and clusters from MCA results.
  - Visualizes relationships between topics such as Fuzzy Logic, Governance, Compliance, and Optimization.
  - Output: `MCA_Conceptual_Structure_Map.png` and `MCA_Conceptual_Structure_Map.svg`.

---

## Project Structure

- `Trends_in_Topics_2000_2024.py` — Script for publication trends visualization.
- `MCA-map.py` — Script for conceptual structure mapping using MCA.
- `requirements.txt` — Python dependencies.
- `*.png` and `*.svg` — Generated visualizations.

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repo-url>
   cd Bibliometric-Visualization-For-Publication
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   # On Unix or MacOS
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

- **Generate Publication Trends Plot:**

  ```bash
  python Trends_in_Topics_2000_2024.py
  ```

  This will create `Trends_in_Topics_2000_2024.png` and `Trends_in_Topics_2000_2024.svg`.

- **Generate MCA Conceptual Structure Map:**
  ```bash
  python MCA-map.py
  ```
  This will create `MCA_Conceptual_Structure_Map.png` and `MCA_Conceptual_Structure_Map.svg`.

---

## Dependencies

Key Python packages (see `requirements.txt` for full list):

- `matplotlib`
- `numpy`
- `lxml`
- `python-pptx`
- `xlsxwriter`

---

## Outputs

- **Publication Trends:**  
  ![Trends_in_Topics_2000_2024.png](Trends_in_Topics_2000_2024.png)

- **MCA Conceptual Structure Map:**  
  ![MCA_Conceptual_Structure_Map.png](MCA_Conceptual_Structure_Map.png)

---

## License

Specify your license here (e.g., MIT, GPL, etc.).
