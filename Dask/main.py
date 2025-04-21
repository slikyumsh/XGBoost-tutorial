from dask.distributed import Client, LocalCluster
import dask.array as da
from dask_ml.datasets import make_classification
import xgboost as xgb
from xgboost.dask import DaskDMatrix, train

def main():
    cluster = LocalCluster()
    client = Client(cluster)

    X, y = make_classification(n_samples=10000000, n_features=20, chunks=1000, random_state=42)

    dtrain = DaskDMatrix(client, X, y)
    params = {'objective': 'binary:logistic', 'tree_method': 'hist', 'eval_metric': 'logloss'}
    output = train(client, params, dtrain, num_boost_round=10)

    bst = output['booster']
    preds = xgb.dask.predict(client, bst, X)
    print(preds.compute()[:10])

if __name__ == "__main__":
    main()
