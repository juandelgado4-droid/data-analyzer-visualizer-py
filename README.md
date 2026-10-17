# 📊 Automated Data Analyzer & Visualizer (Python)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python)](https://python.org)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Stdlib)-success)]()

An automated Exploratory Data Analysis (EDA) and dataset statistical profiling CLI tool built in **Python 3**. Engineered to run out-of-the-box using the Python standard library with zero external runtime dependencies.

---

## ✨ Features

- **Descriptive Numerical Statistics**: Calculates mean, median, sample variance, standard deviation, and min/max boundaries.
- **Dispersion & Quantile Analysis**: Evaluates $Q_1$, $Q_3$, and Interquartile Range (IQR).
- **Outlier Detection via Tukey's Fences**: Automatically flags data anomalies beyond $[Q_1 - 1.5 \times \text{IQR}, Q_3 + 1.5 \times \text{IQR}]$.
- **Bivariate Pearson Correlation Matrix**: Computes pairwise linear correlation coefficients between all numerical attributes.
- **ASCII Histogram Distributions**: Visualizes probability density and value clustering directly inside the terminal.
- **Automated Markdown Export**: Exports complete summary tables ready for documentation and reports.

---

## 🚀 Quick Start / How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/juandelgado4-droid/data-analyzer-visualizer-py.git
   cd data-analyzer-visualizer-py
   ```
2. Run analysis on the included sample dataset:
   ```bash
   python main.py
   ```
3. Run on your own custom CSV dataset and export a Markdown report:
   ```bash
   python main.py --file my_dataset.csv --export-md report.md
   ```

---

## 💻 Sample Output

```
================================================================
      EXPLORATORY DATA ANALYSIS (EDA) STATISTICAL REPORT       
================================================================
[*] Total Records:  20
[*] Total Columns:  6
[*] Numeric Fields: 6 ['id', 'age', 'salary', 'credit_score', 'purchases_per_month', 'tenure_months']

>> Column: [salary]
   Count:   20 | Mean: 93450.0 | StdDev: 49457.025
   Min:     32000.0 | Median: 75000.0 | Max: 220000.0
   IQR:     68500.0 | Detected Outliers: 0
   Distribution Histogram:
  [32000.0 - 63333.3] | ████████████████████ (7)
  [63333.3 - 94666.7] | ██████████████ (5)
  [94666.7 - 126000.0] | ████████ (3)
  [126000.0 - 157333.3] | ███████████ (4)
  [157333.3 - 188666.7] |  (0)
  [188666.7 - 220000.0] | ██ (1)
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
