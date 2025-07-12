Author: Katarzyna Brzeski.
4th-year Informatics student, AI & Data Science specialization


# Intelligent Customer Segmentation

This project focuses on intelligent customer segmentation using clustering techniques. It analyzes real-world e-commerce data (over 540,000 records) to identify distinct customer groups based on their behavior, activity, and geographic origin.

## Project Overview

The goal was to apply and compare clustering algorithms – **K-Means** and **K-Medoids** – with different distance metrics (Euclidean and Manhattan) and different values of k (number of clusters).

### Key Steps:

- Data cleaning and aggregation on the customer level
- Feature engineering (e.g. customer lifespan, average unit price)
- Normalization (Min-Max)
- K-Means clustering (k=2, 3, 6, 8)
- K-Medoids clustering (k=6)
- Distance metrics comparison (Euclidean vs. Manhattan)
- Elbow method for optimal k selection
- Cluster interpretation with real business context
- Visualizations: scatter plots, centroid analysis, distance histograms

## Key Findings

- **K = 6** was selected as the optimal number of clusters for business applications.
- K-Means offers faster convergence and statistically efficient grouping.
- K-Medoids provides more interpretable clusters with real data points as centers, and higher robustness to outliers.
- Clusters revealed meaningful segments such as:
  - One-time buyers,
  - Loyal customers,
  - Premium clients,
  - Region-based differences (e.g. France, Greece, Singapore).

## Files Included

- `Intelligent Data Analysis.pdf` – Full project report with analysis, visuals and interpretation
- notebook/clustering_analysis.ipynb.
-  Dataset 

## Tools & Technologies

- Python (Pandas, NumPy, Scikit-learn, Matplotlib)
- Clustering: KMeans, KMedoids
- Distance metrics: Euclidean, Manhattan
- Visualization: scatter plots, histograms
- PDF prepared for portfolio purposes

## Applications

This type of analysis can support:
- Marketing campaign targeting
- Loyalty strategy design
- Customer retention and churn prediction
- Market segmentation and profiling




