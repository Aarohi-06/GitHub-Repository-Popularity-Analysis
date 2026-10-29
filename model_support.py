"""The original notebook's dummy encoding, packaged for standalone prediction."""
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class NotebookFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, features, encoded_columns, languages):
        self.features = features
        self.encoded_columns = encoded_columns
        self.languages = languages

    def fit(self, X, y=None):
        self.feature_names_in_ = self.features
        self.n_features_in_ = len(self.features)
        return self

    def transform(self, X):
        if not isinstance(X, pd.DataFrame):
            raise ValueError('Inputs must be a dataframe with named features.')
        frame = X.loc[:, self.features].copy()
        if not frame['language'].isin(self.languages).all():
            raise ValueError('Select a language supported by the trained model.')
        for name in self.features:
            if name != 'language':
                frame[name] = pd.to_numeric(frame[name], errors='raise')
                if frame[name].isna().any() or (frame[name] < 0).any():
                    raise ValueError(f'{name} must contain nonnegative numbers.')
        encoded = pd.get_dummies(frame, columns=['language'], dtype=int)
        return encoded.reindex(columns=self.encoded_columns, fill_value=0)


def make_input(language, forks, open_issues, size, age_years, feature_order):
    values = dict(language=language, forks=float(forks), open_issues=float(open_issues),
                  size=float(size), age_years=float(age_years))
    return pd.DataFrame([values], columns=feature_order)
