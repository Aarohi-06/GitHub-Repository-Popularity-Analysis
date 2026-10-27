# GitHub-Repository-Popularity-Analysis
Statistical Inference project analyzing GitHub repository popularity using Python and Machine Learning
# GitHub Repository Popularity Analysis

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

Random Forest performed best in both tasks.

| Task | Best Model | Result |
|---|---|---|
| Regression | Random Forest | R² = 0.904 |
| Classification | Random Forest | Accuracy = 90% |

The classification model predicts whether a repository has **High Popularity** or **Low Popularity** based on its characteristics.

## Technologies Used

Python, Google Colab, Pandas, NumPy, Matplotlib, Seaborn, SciPy, Scikit-learn, BeautifulSoup, Requests, and Gradio.

## How to Run

1. Download or open the `.ipynb` notebook in Google Colab.
2. Run the cells sequentially.
3. The notebook collects and processes GitHub repository data.
4. View the statistical analyses, visualizations, and model evaluation results.
5. Run the final Gradio section to launch the prediction interface.

**Note:** An internet connection is required for GitHub API data collection. The Gradio interface requires the trained classification model.

## Conclusion

The project demonstrates how Statistical Inference and Machine Learning can be used to analyze GitHub repository characteristics and predict popularity. Random Forest achieved the best performance among the tested regression and classification models.

The results are based on the collected repository dataset and should not be generalized to all GitHub repositories.
