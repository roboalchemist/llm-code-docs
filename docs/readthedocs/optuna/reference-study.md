# optuna.study

The `study` module implements the `Study` object and related functions. A public constructor is available for the `Study` class, but direct use of this constructor is not recommended. Instead, library users should create and load a `Study` using `create_study()` and `load_study()` respectively.

`Study`

A study corresponds to an optimization task, i.e., a set of trials.

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

`MaxTrialsCallback`

Set a maximum number of trials before ending the study.

`StudyDirection`

Direction of a `Study`.

`StudySummary`

Basic attributes and aggregated results of a `Study`.