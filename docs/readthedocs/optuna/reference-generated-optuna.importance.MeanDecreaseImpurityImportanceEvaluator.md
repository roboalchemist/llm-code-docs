# optuna.importance.MeanDecreaseImpurityImportanceEvaluator

class optuna.importance.MeanDecreaseImpurityImportanceEvaluator(***, *n_trees=64*, *max_depth=64*, *seed=None*)

Mean Decrease Impurity (MDI) parameter importance evaluator.

This evaluator fits fits a random forest regression model that predicts the objective values
of `COMPLETE` trials given their parameter configurations.
Feature importances are then computed using MDI.

Note

This evaluator requires the sklearn [https://scikit-learn.org/stable/] Python package
and is based on sklearn.ensemble.RandomForestClassifier.feature_importances_ [https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.feature_importances_].