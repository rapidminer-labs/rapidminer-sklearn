import pandas as pd
from sklearn.mixture import GaussianMixture


def rm_train(X, params):
    print(params)
    model = GaussianMixture(**params).fit(X)
    bic_score = model.bic(X)
    return model, pd.DataFrame({"BIC": bic_score},index=[1])


def rm_apply(X, model):
    prediction = pd.DataFrame(model.score_samples(X))
    prediction.columns = ['Anomaly_Score']
    return prediction
