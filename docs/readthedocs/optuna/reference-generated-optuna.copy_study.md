# optuna.copy_study

optuna.copy_study(***, *from_study_name*, *from_storage*, *to_storage*, *to_study_name=None*)

Copy study from one storage to another.

The direction(s) of the objective(s) in the study, trials, user attributes and system
attributes are copied.

Note

`copy_study()` copies a study even if the optimization is working on.
It means users will get a copied study that contains a trial that is not finished.