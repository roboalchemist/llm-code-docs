# optuna.importance.FanovaImportanceEvaluator

class optuna.importance.FanovaImportanceEvaluator(***, *n_trees=64*, *max_depth=64*, *seed=None*)

fANOVA importance evaluator.

Implements the fANOVA hyperparameter importance evaluation algorithm in
An Efficient Approach for Assessing Hyperparameter Importance [http://proceedings.mlr.press/v32/hutter14.html].

fANOVA fits a random forest regression model that predicts the objective values
of `COMPLETE` trials given their parameter configurations.
The more accurate this model is, the more reliable the importances assessed
by this class are.

Note

Requires the sklearn [https://github.com/scikit-learn/scikit-learn] Python package.