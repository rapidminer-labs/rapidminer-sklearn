import pandas as pd
from sklearn.mixture import GaussianMixture


def rm_train(X, params):
    print(params)
    model = GaussianMixture(**params).fit(X)
    anom = model.bic(X)
    return {"model": model, "bic": anom}


def rm_apply(X, container):
    model = container['model']
    prediction = pd.DataFrame(model.score_samples(X))
    prediction.columns = ['Anomaly_Score']
    return prediction
