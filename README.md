# Parkinson’s Disease Hypothesis Testing Using Data Science

This repository contains the code and resources for the project titled **"Leveraging Data Science for Hypothesis Testing in Parkinson’s Disease Research"**. The project applies statistical hypothesis testing methods to biomedical voice datasets to identify acoustic features that significantly differentiate Parkinson’s Disease (PD) patients from healthy controls.

## Project Overview

Parkinson’s Disease is a progressive neurodegenerative disorder characterized by motor and vocal impairments. Early diagnosis is crucial for effective management. This project utilizes the publicly available UCI Parkinson’s Disease voice dataset and applies independent two-sample t-tests to quantify differences in voice features such as Mean Fundamental Frequency, Jitter, Shimmer, and Harmonic-to-Noise Ratio.

The aim is to statistically validate non-invasive biomarkers that can enable telemonitoring and improved clinical diagnostics through data science methodologies.

## Repository Contents

- `parkinsons_analysis.py` — Python script performing data loading, preprocessing, hypothesis testing, and visualization.
- `README.md` — This file.
- `results/` — Folder containing output tables and plots generated from analysis.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries:
  - pandas
  - scipy
  - matplotlib
  - seaborn

Install dependencies with: 
```bash
pip install pandas scipy matplotlib seaborn
```
### Dataset

Download the Parkinson’s Disease voice dataset from UCI Machine Learning Repository:  
[https://archive.ics.uci.edu/ml/datasets/parkinsons](https://archive.ics.uci.edu/ml/datasets/parkinsons)

Place the downloaded `parkinsons.data` file in the root directory of this repository or update the path in the script accordingly.

### Running the Analysis

Run the main analysis script: 
```bash
python parkinsons_analysis.py
```

This will load the data, perform preprocessing, execute hypothesis testing on selected features, and generate relevant plots and summary tables.

## Results

- Statistical test results indicating significant voice feature differences between PD patients and controls.
- Boxplots visualizing feature distributions.
- Summary table (Table 1) in the output folder.

## Citation

If you use or refer to this repository, please cite as follows:

T. S. Chauhan, "Parkinson’s Disease Hypothesis Testing Code," GitHub repository, [Online]. Available: https://github.com/tanujsinghchauhan/Parkinsons-Disease-Hypothesis-testing. [Accessed: Date].

## Contact

For questions or collaboration, please open an issue or contact [tanujsinghchauhan38.email@example.com].

---

*This project was developed as part of a data science research effort focused on healthcare applications and Parkinson’s Disease.*
