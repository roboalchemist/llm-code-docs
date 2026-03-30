# optuna

The `optuna` module is primarily used as an alias for basic Optuna functionality coded in other modules. Currently, two modules are aliased: (1) from `optuna.study`, functions regarding the Study lifecycle, and (2) from `optuna.exceptions`, the TrialPruned Exception raised when a trial is pruned.

`create_study`

Create a new `Study`.

`load_study`

Load the existing `Study` that has the specified name.

`delete_study`

Delete a `Study` object.

`copy_study`

Copy study from one storage to another.

`get_all_study_names`

Get all study names stored in a specified storage.

`get_all_study_summaries`

Get all history of studies stored in a specified storage.

`TrialPruned`

Exception for pruned trials.