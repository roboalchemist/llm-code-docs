# optuna.pruners

The `pruners` module defines a `BasePruner` class characterized by an abstract `prune()` method, which, for a given trial and its associated study, returns a boolean value representing whether the trial should be pruned. This determination is made based on stored intermediate values of the objective function, as previously reported for the trial using `optuna.trial.Trial.report()`. The remaining classes in this module represent child classes, inheriting from `BasePruner`, which implement different pruning strategies.

Warning

Currently `pruners` module is expected to be used only for single-objective optimization.