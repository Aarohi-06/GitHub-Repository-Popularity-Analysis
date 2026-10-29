# GitHub Repository Popularity Analysis

Uses Aarohi's original `B3_B1_01_Aarohi_Nagdeote.ipynb` unchanged, including its practicals, code, markdown, graphs and saved outputs. Streamlit runs separately without Gradio or GitHub API access.

## Launch (PowerShell, from this project folder)

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open http://localhost:8501. Select programming language and enter forks, open issues, size in KB and age in years. Saved preprocessing and model load automatically.

## Actual results

The real cleaned CSV was found in Downloads as `B3_B1_01_Aarohi Nagdeote_github_cleaned_data.csv` and copied byte-for-byte to `data/github_cleaned_data.csv`. It matches the original notebook's saved records: 600 rows, 100 per language, no duplicate names or missing essential fields. No API collection or synthetic data was used. Saved `age_years` values are retained to reproduce original inputs.

- Selected model: **Decision Tree**, max_depth=4, random_state=42.
- Test accuracy: **83.33%** (0.8333333333333334).
- Test F1: **0.8148148148148148**.
- Training/test rows: **480 / 120**, original 80/20 split, seed 42.
- Popularity cutoff: training median **74.5 stars**. High=1 means strictly above cutoff; Low=0 otherwise.
- Raw feature order: forks, open_issues, size, age_years, language. Stars are never an input.
- Original models: scaled Logistic Regression, scaled SVM, depth-4 Decision Tree, depth-6 Random Forest with 100 trees, scaled KNN with 5 neighbors.
- Selection: highest held-out test F1, exactly as in the original notebook. This classroom comparison uses the test set to select the model; metrics are not independent validation results. The collected sample is not representative of all GitHub repositories.

Full model comparisons are saved in `models/model_comparison.csv`; the fitted model, exact preprocessing and feature order are in `models/popularity_pipeline.joblib`. `models/metadata.joblib` contains actual metrics, labels, cutoff and notebook/dataset hashes.

## Project files

- `B3_B1_01_Aarohi_Nagdeote.ipynb`: untouched original notebook with saved results.
- `app.py`: working Streamlit interface.
- `model_support.py`: required application dependency; defines the preprocessing class embedded in the saved pipeline and the input schema. Do not remove it.
- `data/github_cleaned_data.csv`: preserved real 600-repository dataset.
- `models/popularity_pipeline.joblib`: fitted preprocessing and selected classifier together.
- `models/metadata.joblib`: feature order, label mapping, actual metrics and provenance.
- `models/model_comparison.csv`: evaluation comparison displayed by Streamlit.
- `requirements.txt`: installed dependency versions.
- `.venv/`: existing Python environment, preserved.

The trained pipeline was verified against the original notebook's dummy encoding and held-out predictions. Fresh-process loading, Streamlit rendering, actual form submission and prediction were tested. Unused training/test scripts, duplicate standalone classifier/preprocessing artifacts and the redundant JSON report were removed after checking runtime dependencies. Retraining remains possible using the original notebook's classification cells; the saved application requires no training or network requests.

## Notebook environment

A kernel named **SI Project (.venv)** uses the same existing environment as Streamlit. Launch Jupyter with:

```powershell
.\.venv\Scripts\python.exe -m notebook B3_B1_01_Aarohi_Nagdeote.ipynb
```

Select **SI Project (.venv)**. The original notebook intentionally retains its original Colab download, Gradio and network cells. Demonstrate its saved analysis outputs directly. Running all original cells locally would still invoke those original operations. The Streamlit app loads its saved artifacts independently of notebook execution. The notebook file was verified by SHA256 to remain unchanged.

`requirements.txt` records the installed versions needed for training, Streamlit and the original statistical analysis. Gradio is unnecessary for the Streamlit app and is omitted.
