# optuna.exceptions.TrialPruned

exception optuna.exceptions.TrialPruned

Exception for pruned trials.

This error tells a trainer that the current `Trial` was pruned. It is
supposed to be raised after `optuna.trial.Trial.should_prune()` as shown in the following
example.

See also

`optuna.TrialPruned` is an alias of `optuna.exceptions.TrialPruned`.