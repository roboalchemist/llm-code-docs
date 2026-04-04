# Source: https://docs.vespa.ai/en/ranking/xgboost.html.md

# Ranking with XGBoost Models

 

Vespa supports importing Gradient Boosting Decision Tree (GBDT) models trained with XGBoost.

 **Warning:** Vespa only supports XGBoost models trained with XGBoost version 1.5 or earlier. Using models trained with later versions of XGBoost may result in prediction mismatches between Vespa and XGBoost's native predict functions.

## Exporting models from XGBoost

Vespa supports importing XGBoost's JSON model dump, e.g. Python API[xgboost.Booster.dump\_model](https://xgboost.readthedocs.io/en/latest/python/python_api.html#xgboost.Booster.dump_model). When dumping the trained model, XGBoost allows users to set the `dump_format` to `json`, and users can specify the feature names to be used in `fmap`.

Here is an example of an XGBoost JSON model dump with 2 trees and maximum depth 1:

```
```
[
  { "nodeid": 0, "depth": 0, "split": "fieldMatch(title).completeness", "split_condition": 0.772132337, "yes": 1, "no": 2, "missing": 1, "children": [
    { "nodeid": 1, "leaf": 0.673938096 },
    { "nodeid": 2, "leaf": 0.791884363 }
  ]},
  { "nodeid": 0, "depth": 0, "split": "fieldMatch(title).importance", "split_condition": 0.606320798, "yes": 1, "no": 2, "missing": 1, "children": [
    { "nodeid": 1, "leaf": 0.469432801 },
    { "nodeid": 2, "leaf": 0.55586201 }
  ]}
]
```
```

Notice the `split` attribute which represents the Vespa feature name. The `split` feature must resolve to a Vespa[rank feature](../reference/ranking/rank-features.html) defined in the [document schema](../basics/schemas.html). The feature can also be user defined features (for example using [functions](ranking-expressions-features.html#function-snippets)).

The above model JSON was produced using the XGBoost Python api with a regression objective:

```
```
#!/usr/local/bin/python3
import xgboost as xgb

dtrain = xgb.DMatrix('training-vectors.txt')
param = {'base_score':0, 'max_depth':1,'objective':'reg:squarederror'}
bst = xgb.train(param, dtrain, 2)
bst.dump_model("trained-model.json",fmap='feature-map.txt', with_stats=False, dump_format='json')
```
```

The training data is represented using [LibSVM text format](https://xgboost.readthedocs.io/en/latest/tutorials/input_format.html). See also a complete [XGBoost training notebook](https://github.com/vespa-engine/sample-apps/blob/master/commerce-product-ranking/notebooks/Train-xgboost.ipynb) using `ranking` objective.

## Feature mappings from XGBoost to Vespa

XGBoost is trained on array or array like data structures where features are named based on the index in the array as in the example above. To convert the XGBoost features we need to map feature indexes to actual Vespa features (native features or custom defined features):

```
$ cat feature-map.txt |egrep "fieldMatch\(title\).completeness|fieldMatch\(title\).importance"
36 fieldMatch(title).completeness q
39 fieldMatch(title).importance q
```

In the feature mapping example, feature at index 36 maps to[fieldMatch(title).completeness](../reference/ranking/rank-features.html#fieldMatch(name).completeness)and index 39 maps to [fieldMatch(title).importance](../reference/ranking/rank-features.html#fieldMatch(name).importance). The feature mapping format is not well described in the XGBoost documentation,but the [sample demo for binary classification](https://github.com/dmlc/xgboost/tree/master/demo) writes:

Format of `feature-map.txt: <featureid> <featurename> <q or i or int>\n`:

- "Feature id" must be from 0 to number of features, in sorted order.
- "i" means this feature is binary indicator feature
- "q" means this feature is a quantitative value, such as age, time, can be missing
- "int" means this feature is integer value (when int is hinted, the decision boundary will be integer)

When using `pandas``DataFrame`'s with columns names, one does not need to provide feature mappings.

See also a complete example of how to train a ranking function, using learning to rank with ranking losses, in this [notebook](https://github.com/vespa-engine/sample-apps/blob/master/commerce-product-ranking/notebooks/Train-xgboost.ipynb).

## Importing XGBoost models

To import the XGBoost model to Vespa, add the directory containing the model to your application package under a specific directory named `models`. For instance, if you would like to call the model above as `my_model`, you would add it to the application package resulting in a directory structure like this:

```
├── models
│   └── my_model.json
├── schemas
│   └── main.sd
└── services.xml
```

An application package can have multiple models.

## Ranking with XGBoost models

Vespa has a `xgboost` [ranking feature](../reference/ranking/rank-features.html). This ranking feature specifies the model to use in a ranking expression. Consider the following example:

```
schema xgboost {
    rank-profile prediction inherits default {
        first-phase {
          expression: nativeRank
        }
        second-phase {
            expression: xgboost("my_model.json")
        }
    }
}
```

Here, we specify that the model `my_model.json` is applied to the top ranking documents by the first-phase ranking expression. The query request must specify `prediction` as the [ranking.profile](../reference/api/query.html#ranking.profile). See also [Phased ranking](phased-ranking.html) on how to control number of data points/documents which is exposed to the model.

Generally the run time complexity is determined by:

- The number of documents evaluated [per thread](../performance/sizing-search.html) / number of nodes and the query filter
- The complexity of computing features. For example `fieldMatch` features are 100x more expensive that `nativeFieldMatch/nativeRank`.
- The number of XGboost trees and the maximum depth per tree

Serving latency can be brought down by [using multiple threads per query request](../performance/practical-search-performance-guide.html#multithreaded-search-and-ranking).

## XGBoost models

There are six different [objective](https://xgboost.readthedocs.io/en/stable/parameter.html#learning-task-parameters) types that Vespa supports:

- Regression `reg:squarederror` / `reg:logistic`
- Classification `binary:logistic`
- Ranking `rank:pairwise`, `rank:ndcg` and `rank:map`

For `reg:logistic` and `binary:logistic` the raw margin tree sum (Sum of all trees) needs to be passed through the sigmoid function to represent the probability of class 1. For regular regression the model can be directly imported but the `base_score` should be set 0 as the `base_score` used during the training phase is not dumped with the model.

An example model using the sklearn toy datasets is given below:

```
```
from sklearn import datasets
import xgboost as xgb
breast_cancer = datasets.load_breast_cancer()
c = xgb.XGBClassifier(n_estimators=20, objective='binary:logistic')
c.fit(breast_cancer.data,breast_cancer.target) 
c.get_booster().dump_model("binary_breast_cancer.json", fmap='feature-map.txt', dump_format='json')
c.predict_proba(breast_cancer.data)[:,1]
```
```

To represent the `predict_proba` function of XGBoost for the binary classifier in Vespa, we need to use the [sigmoid function](../reference/ranking/ranking-expressions.html):

```
schema xgboost {
    rank-profile prediction-binary inherits default {
        first-phase {
            expression: sigmoid(xgboost("binary_breast_cancer.json"))
        }
    }
}
```

## Debugging Vespa inference score versus XGBoost predict score

- When dumping XGBoost models to a JSON representation some of the model information is lost (e.g. the `base_score` or the optimal number of trees if trained with early stopping). XGBoost also has different predict functions (e.g. predict/predict\_proba). The following [XGBoost System Test](https://github.com/vespa-engine/system-test/tree/master/tests/search/xgboost)demonstrates how to represent different type of XGBoost models in Vespa.
- For training, features should be scraped from Vespa, using either `match-features` or `summary-features` so that features from offline training matches the online Vespa computed features. Dumping features can also help debug any differences by zooming into specific query,document pairs using [recall](../reference/api/query.html#recall) parameter.
- It's also important to use the highest possible precision when reading Vespa features for training as Vespa outputs features using `double` precision. If the training routine rounds features to `float` or other more compact floating number representations, feature split decisions might differ in Vespa versus XGboost.
- In a distributed setting when multiple nodes uses the model, text matching features such as `nativeRank`, `nativFieldMatch`, `bm25` and `fieldMatch`might differ, depending on which node produced the hit. The reason is that all these features use [term(n).significance](../reference/ranking/rank-features.html#query-features), which is computed locally indexed corpus. The `term(n).significance` feature is related to _Inverse Document Frequency (IDF)_. The `term(n).significance` should be set by a searcher in the container for global correctness as each node will estimate the significance values from the local corpus.

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Exporting models from XGBoost](#exporting-models-from-xgboost)
- [Feature mappings from XGBoost to Vespa](#feature-mappings-from-xgboost-to-vespa)
- [Importing XGBoost models](#importing-xgboost-models)
- [Ranking with XGBoost models](#ranking-with-xgboost-models)
- [XGBoost models](#xgboost-models)
- [Debugging Vespa inference score versus XGBoost predict score](#debugging-vespa-inference-score-versus-xgboost-predict-score)

