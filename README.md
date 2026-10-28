# GitHub Repository Popularity Analysis

Statistical Inference project analyzing GitHub repository popularity using Python and Machine Learning.

## Project Overview

This project analyzes the popularity of GitHub repositories using Statistical Inference and Machine Learning techniques.

The project collects GitHub repository data, performs exploratory data analysis, applies statistical methods, and uses machine learning models to predict repository popularity.

It was developed as part of the **Statistical Inference (SI) Lab Project** for Semester V.

## Objectives

- Collect repository data using the GitHub API and demonstrate web scraping using BeautifulSoup.
- Clean and analyze repository data.
- Apply sampling methods and the Central Limit Theorem.
- Perform hypothesis testing and correlation analysis.
- Compare regression models to predict repository stars.
- Compare classification models to predict High or Low popularity.
- Develop a simple Gradio interface for popularity prediction.

## Dataset

The dataset contains **600 GitHub repositories** collected across six programming languages:

- Python
- JavaScript
- Java
- C++
- Go
- Rust

The dataset includes repository stars, forks, open issues, size, programming language, and repository age.

**Data Source:** [GitHub REST API](https://docs.github.com/en/rest)

## Project Implementation

| Practical | Implementation |
|---|---|
| 1 | Web Scraping and Data Collection |
| 2 | Data Cleaning, EDA and Visualization |
| 3 | Distributions and Sampling |
| 4 | Central Limit Theorem |
| 5 | Hypothesis Testing (T-test, ANOVA, Chi-Square) |
| 6 | Covariance and Correlation |
| 7 | Regression |
| 8 | Classification |
| 9 | Gradio User Interface |

## Machine Learning Models

**Regression Models:**
- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor

**Classification Models:**
- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)

## Results

Random Forest achieved the best regression performance, while Decision Tree achieved the highest F1-score in classification.

### Regression Results

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Random Forest | 1200.458 | 4546.696 | 0.467 |
| Decision Tree | 1284.352 | 4802.827 | 0.406 |
| Lasso Regression | 1761.275 | 5195.648 | 0.305 |
| Linear Regression | 1761.352 | 5195.701 | 0.305 |
| Ridge Regression | 1762.286 | 5196.306 | 0.304 |

### Classification Results

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Decision Tree | 0.833 | 0.772 | 0.863 | 0.815 |
| Random Forest | 0.825 | 0.788 | 0.804 | 0.796 |
| Logistic Regression | 0.700 | 0.674 | 0.569 | 0.617 |
| KNN | 0.667 | 0.608 | 0.608 | 0.608 |
| SVM | 0.625 | 0.560 | 0.549 | 0.554 |

**Best Regression Model:** Random Forest (R² = 0.467)

**Best Classification Model:** Decision Tree (Accuracy = 83.3%, F1-Score = 0.815)

The classification model predicts whether a repository has **High Popularity** or **Low Popularity** based on its characteristics.

## Gradio User Interface

A simple interactive Gradio interface is implemented in the notebook to predict GitHub repository popularity.

Users can provide repository characteristics such as:

- Programming language
- Number of forks
- Number of open issues
- Repository size (KB)
- Repository age (years)

The interface uses the selected classification model to predict whether the repository has **High Popularity** or **Low Popularity**.

## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Scikit-learn
- BeautifulSoup
- Requests
- Gradio

## How to Run

1. Download or open the `.ipynb` notebook in Google Colab.
2. Run the cells sequentially.
3. The notebook collects and processes GitHub repository data.
4. View the statistical analyses, visualizations, and model evaluation results.
5. Run the final Gradio section to launch the prediction interface.
6. Enter repository details to predict High or Low popularity.

**Note:** An internet connection is required for GitHub API data collection. The Gradio interface requires the trained classification model and preprocessing steps to be available in the notebook session.

## Conclusion

The project demonstrates how Statistical Inference and Machine Learning can be used to analyze GitHub repository characteristics and predict popularity.

Random Forest achieved the best regression performance with an R² score of 0.467, while Decision Tree achieved the best classification F1-score of 0.815 and an accuracy of 83.3%.

The results are based on the collected repository dataset and should not be generalized to all GitHub repositories.
