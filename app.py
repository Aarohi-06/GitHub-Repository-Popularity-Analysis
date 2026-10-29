"""Streamlit prediction interface for the original notebook's fitted classifier."""
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

from model_support import make_input

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title='GitHub Repository Popularity Analysis', page_icon='📊', layout='centered')
st.title('GitHub Repository Popularity Analysis')
st.caption('Predict repository popularity using the classification approach in the original notebook.')


@st.cache_resource
def load_artifacts():
    return (joblib.load(ROOT / 'models' / 'popularity_pipeline.joblib'),
            joblib.load(ROOT / 'models' / 'metadata.joblib'))


try:
    pipeline, metadata = load_artifacts()
except Exception as error:
    st.error(f'Cannot load trained model: {error}')
    st.info('Restore the trained pipeline and metadata in the models folder, then restart the app.')
    st.stop()

st.subheader('Repository details')
with st.form('repository_details'):
    language = st.selectbox('Programming language', metadata['languages'])
    left, right = st.columns(2)
    with left:
        forks = st.number_input('Repository forks', min_value=0, value=50, step=1)
        size = st.number_input('Repository size (KB)', min_value=0, value=1000, step=100)
    with right:
        open_issues = st.number_input('Open issues', min_value=0, value=10, step=1)
        age_years = st.number_input('Repository age (years)', min_value=0.0, value=3.0, step=0.1)
    submitted = st.form_submit_button('Predict Popularity', type='primary', use_container_width=True)

if submitted:
    try:
        row = make_input(language, forks, open_issues, size, age_years, metadata['feature_order'])
        prediction = int(pipeline.predict(row)[0])
        st.success(f"Predicted category: {metadata['label_mapping'][prediction]}")
    except (ValueError, TypeError, KeyError) as error:
        st.error(f'Prediction failed: {error}')

st.divider()
st.subheader(f"Trained model: {metadata['model_name']}")
accuracy, f1 = st.columns(2)
accuracy.metric('Test accuracy', f"{metadata['metrics']['Accuracy']:.2%}")
f1.metric('Test F1-score', f"{metadata['metrics']['F1']:.4f}")
st.caption(f"Selected by highest test F1 • {metadata['train_rows']} training / {metadata['test_rows']} test repositories")
st.write(f"High popularity means stars strictly above the training median of **{metadata['cutoff_stars']:g}**. Stars are not an input feature.")
with st.expander('Model comparison and project details'):
    st.dataframe(pd.read_csv(ROOT / 'models' / 'model_comparison.csv'), hide_index=True)
    st.write('Original notebook: B3_B1_01_Aarohi_Nagdeote.ipynb')
    st.write('The collected repository sample is not representative of all GitHub repositories. Metrics use the same test-set selection approach as the original classroom notebook.')
    st.caption('Predictions run locally using saved artifacts. No GitHub requests or Gradio are required.')
