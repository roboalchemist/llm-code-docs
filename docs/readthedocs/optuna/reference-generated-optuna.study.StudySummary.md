# optuna.study.StudySummary

class optuna.study.StudySummary(*study_name*, *direction*, *best_trial*, *user_attrs*, *system_attrs*, *n_trials*, *datetime_start*, *study_id*, ***, *directions=None*)

Basic attributes and aggregated results of a `Study`.

See also `optuna.study.get_all_study_summaries()`.

Parameters:

- 

**study_name** (*str* [https://docs.python.org/3/library/stdtypes.html#str])

- 

**direction** (*StudyDirection** | **None*)

- 

**best_trial** (*FrozenTrial** | **None*)

- 

**user_attrs** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]*[**str* [https://docs.python.org/3/library/stdtypes.html#str]*, **Any**]*)

- 

**system_attrs** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]*[**str* [https://docs.python.org/3/library/stdtypes.html#str]*, **Any**]*)

- 

**n_trials** (*int* [https://docs.python.org/3/library/functions.html#int])

- 

**datetime_start** (*datetime.datetime* [https://docs.python.org/3/library/datetime.html#datetime.datetime]* | **None*)

- 

**study_id** (*int* [https://docs.python.org/3/library/functions.html#int])

- 

**directions** (*Sequence**[**StudyDirection**] **| **None*)

study_name

Name of the `Study`.

direction

`StudyDirection` of the `Study`.

Note

This attribute is only available during single-objective optimization.