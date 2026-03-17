# optuna.importance.PedAnovaImportanceEvaluator

class optuna.importance.PedAnovaImportanceEvaluator(***, *target_quantile=0.1*, *region_quantile=1.0*, *baseline_quantile=None*, *evaluate_on_local=True*)

PED-ANOVA importance evaluator.

Implements the PED-ANOVA hyperparameter importance evaluation algorithm.

PED-ANOVA fits Parzen estimators of `COMPLETE` trials better
than a user-specified target_quantile.
The importance can be interpreted as how important each hyperparameter is to get
the performance better than target_quantile.

For further information about PED-ANOVA algorithm, please refer to the following paper:

- 

PED-ANOVA: Efficiently Quantifying Hyperparameter Importance in Arbitrary Subspaces [https://arxiv.org/abs/2304.10255]

target_quantile and region_quantile correspond to the parameters `gamma'` and `gamma`
in the original paper, respectively.

Note

The performance of PED-ANOVA depends on how many trials to consider above
target_quantile. To stabilize the analysis, it is preferable to include at least
5 trials above target_quantile.