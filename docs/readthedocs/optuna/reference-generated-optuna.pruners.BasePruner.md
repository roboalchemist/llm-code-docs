# optuna.pruners.BasePruner

class optuna.pruners.BasePruner

Base class for pruners.

Methods

`prune`(study, trial)

Judge whether the trial should be pruned based on the reported values.

abstractmethod prune(*study*, *trial*)

Judge whether the trial should be pruned based on the reported values.

Note that this method is not supposed to be called by library users. Instead,
`optuna.trial.Trial.report()` and `optuna.trial.Trial.should_prune()` provide
user interfaces to implement pruning mechanism in an objective function.

Parameters:

- 

**study** (*optuna.study.Study*) – Study object of the target study.

- 

**trial** (*optuna.trial.FrozenTrial*) – FrozenTrial object of the target trial.
Take a copy before modifying this object.

Returns:

A boolean value representing whether the trial should be pruned.

Return type:

bool [https://docs.python.org/3/library/functions.html#bool]