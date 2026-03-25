# optuna.exceptions

The `exceptions` module defines Optuna-specific exceptions deriving from a base `OptunaError` class. Of special importance for library users is the `TrialPruned` exception to be raised if `optuna.trial.Trial.should_prune()` returns `True` for a trial that should be pruned.

`OptunaError`

Base class for Optuna specific errors.

`TrialPruned`

Exception for pruned trials.

`CLIUsageError`

Exception for CLI.

`StorageInternalError`

Exception for storage operation.

`DuplicatedStudyError`

Exception for a duplicated study name.

`UpdateFinishedTrialError`

Exception for updating a finished trial.